from contextlib import asynccontextmanager
from typing import Annotated


import uvicorn
from fastapi import FastAPI, Path
from pydantic import BaseModel, EmailStr
from core.config import settings
from items_views import router as item_routers
from users.views import router as users_router
from core.models import Base, db_helper
from api_v1 import router as router_v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engene.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(item_routers)
app.include_router(users_router)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("1:app", reload=True)
