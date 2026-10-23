from dataclasses import dataclass


@dataclass
class UserModel:
    user_id: int
    name: str
    email: str
    password: str
    token: str | None = None
