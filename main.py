from typing import Annotated
from fastapi import FastAPI, Path
from pydantic import BaseModel, EmailStr

import uvicorn

app = FastAPI()

class CreateUser(BaseModel):
    email: EmailStr

@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.get("/items/")
def items():
    return {
        "ITEM1",
        "ITEM2",
        "ITEM3"
    }
@app.get("/items/latest/")
def get_latest_item():
    return {
        "latest":{
            "id": "1",
            "name": "latest"
        }
    }
@app.get("/items/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=555)]):
    return {
        "item": {
            "id": item_id
        }
    }

@app.post("/users/")
def create_user(user: CreateUser):
    return {
        "message": "seccess",
        "email": user.email
    }


# if __name__ == "__main__":
#     uvicorn.run("1:app", reload=True)