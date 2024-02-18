"""This is a boilerplate for an HTTP client provided by pystarter. Please remove this content during development."""

from typing import Optional, Mapping, Any
import requests


class BaseHttpClient:
    """This base class is a boiler template for an HTTP client. Please remove this content during development."""

    BASE_URL = "http://localhost:5000"

    def __init__(self, user_name: str, password: str):
        self.user_name = user_name
        self.password = password
        self.session = requests.Session()
        self.request_token = None

    def authenticate(self):
        """Authenticates the user and sets the request token."""
        response = self.session.post(
            f"{self.BASE_URL}/authenticate",
            json={"user_name": self.user_name, "password": self.password},
        )
        response.raise_for_status()
        data = response.json()
        self.request_token = data["token"]

    def set_request_headers(self, token: str):
        """Sets the request headers with the token."""
        return {"Authorization": f"Bearer {token}"}

    def _request(
        self,
        method: str,
        endpoint: str,
        body: Optional[Mapping[str, Any]] = None,
        params: Optional[Mapping[str, str]] = None,
    ):
        """Makes an HTTP request to the API."""
        headers = self.set_request_headers(self.request_token)
        response = self.session.request(
            method,
            f"{self.BASE_URL}/{endpoint}",
            json=body,
            params=params,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    def get(self, endpoint: str, params: Optional[Mapping[str, str]] = None):
        """Makes a GET request to the API."""
        return self._request("GET", endpoint, params=params)

    def post(self, endpoint: str, body: Optional[Mapping[str, Any]] = None):
        """Makes a POST request to the API."""
        return self._request("POST", endpoint, body=body)

    def put(self, endpoint: str, body: Optional[Mapping[str, Any]] = None):
        """Makes a PUT request to the API."""
        return self._request("PUT", endpoint, body=body)

    def delete(self, endpoint: str, body: Optional[Mapping[str, Any]] = None):
        """Makes a DELETE request to the API."""
        return self._request("DELETE", endpoint, body=body)

    def patch(self, endpoint: str, body: Optional[Mapping[str, Any]] = None):
        return self._request("PATCH", endpoint, body=body)
