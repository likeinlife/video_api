from pydantic import BaseModel


class UserRegisterSchema(BaseModel):
    login: str
    password: str


class UserLoginSchema(UserRegisterSchema): ...
