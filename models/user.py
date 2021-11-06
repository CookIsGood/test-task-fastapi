from typing import Optional
from pydantic import BaseModel, EmailStr, validator, AnyUrl
import re


class UserOut(BaseModel):
    phone: str
    email: EmailStr
    comment: str


class UserIn(BaseModel):
    phone: str
    email: EmailStr
    comment: str

    @validator('phone')
    def check_valid_phone(cls, v):
        match = re.fullmatch(r"[8][0-9]{10}", v)
        if match and len(v) == 11:
            return v
        raise ValueError("Error phone message")

    @validator('comment')
    def check_valid_comment(cls, v):
        match = re.findall(r"(https?://[^\s]+)", v)
        if len(match) == 0:
            return v
        raise ValueError("Error comment message")


class ImageOut(BaseModel):
    image: AnyUrl
