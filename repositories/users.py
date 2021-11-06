from typing import List
from models.user import UserOut, UserIn
from db.users import users
from .base import BaseRepository


class UserRepository(BaseRepository):
    async def get_all(self, limit: int = 100, skip: int = 0) -> List[UserOut]:
        query = users.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query)

    async def create(self, user: UserIn) -> UserOut:
        user = UserOut(
            phone=user.phone,
            email=user.email,
            comment=user.comment
        )
        values = {**user.dict()}
        query = users.insert().values(**values)
        return await self.database.execute(query)

    async def get_user_by_email(self, email: str):
        query = users.select().where(users.c.email == email)
        user = await self.database.fetch_one(query)

        if user is None:
            return None
        return UserOut.parse_obj(user)
