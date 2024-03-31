from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from schemas.user import UserDto
from typing import List
from db.crud import (
    get_user_by_id,
    list_all_users,
)
from sqlalchemy.orm import Session
from pprint import pprint

routes_user = APIRouter()


@routes_user.get("/users/{user_id}", response_model=UserDto, tags=["user"])
async def get_user(user_id: str, request: Request) -> UserDto:
    db: Session = request.state.db
    params = get_user_by_id(db, user_id=user_id)
    if params is None:
        return JSONResponse(status_code=404, content={"message": "Process not found"})
    return params


@routes_user.get("/users", response_model=List[UserDto], tags=["users"])
async def get_processes(request: Request) -> List[UserDto]:
    db: Session = request.state.db
    users = list_all_users(db)
    if users is None:
        return JSONResponse(status_code=404, content={"message": "Process not found"})
    return users
