from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from fastapi import FastAPI, Request
from os import getenv
from dotenv import load_dotenv
from routes.user import routes_user
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()

MYSQL_DB_PASSWORD = getenv("DB_PASSWORD")
MYSQL_ENGINE = getenv("MYSQL_ENGINE")
MYSQL_PORT = getenv("MYSQL_PORT")
MYSQL_DATABASE = getenv("MYSQL_DATABASE")
MYSQL_DB_URL = f"mysql+{MYSQL_ENGINE}://root:{MYSQL_DB_PASSWORD}@localhost:{MYSQL_PORT}/{MYSQL_DATABASE}"

engine = create_engine(MYSQL_DB_URL, connect_args={})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)

app.include_router(routes_user)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next: callable):
    response = None
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response
