from sqlalchemy.ext.asyncio import (
    async_session,
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
)
from sqlalchemy.orm import sessionmaker
from asyncio import current_task
from core.config import settings


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engene = create_async_engine(url=url, echo=echo)
        self.session_make = async_sessionmaker(
            bind=self.engene,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_scope_session(self):
        session = async_scoped_session(
            session_factory=self.session_make, scopefunc=current_task
        )

        return session

    async def session_dependency(self) -> async_session:
        async with self.session_make() as session:
            yield session
            await session.close()

    async def scoped_session_dependency(self) -> async_session:
        session = self.get_scope_session()
        yield session
        await session.close()


db_helper = DatabaseHelper(
    url=settings.db_url,
    echo=settings.db_echo,
)
