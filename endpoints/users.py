from typing import List
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import PlainTextResponse
from models.user import UserOut, UserIn, ImageOut
from repositories.users import UserRepository
from .depends import get_user_repository
from fastapi.encoders import jsonable_encoder

router = APIRouter()


@router.get("/", response_model=List[UserOut])
async def read_users(
        users: UserRepository = Depends(get_user_repository),
        limit: int = 100,
        skip: int = 0,
):
    return await users.get_all(limit=limit, skip=skip)


@router.post("/", response_class=PlainTextResponse)
async def create(
        user: UserIn,
        users: UserRepository = Depends(get_user_repository)
):
    result = await users.get_user_by_email(user.email)
    if result:
        raise HTTPException(status_code=404, detail="User already exist!")
    else:
        await users.create(user=user)
        return "OK"


@router.post("/image", response_class=PlainTextResponse)
async def get_url_image(image: ImageOut):
    image_url = str(jsonable_encoder(image)['image'])
    return f"{image_url}"
