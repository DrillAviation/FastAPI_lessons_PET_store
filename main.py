from typing import Annotated

import uvicorn
from fastapi import FastAPI, Path
from pydantic import BaseModel, EmailStr

from items_views import router as item_routers
from users.views import router as users_router

app = FastAPI()
app.include_router(item_routers)
app.include_router(users_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


# if __name__ == "__main__":
#     uvicorn.run("1:app", reload=True)
