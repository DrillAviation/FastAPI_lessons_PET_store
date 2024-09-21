from typing import Annotated

from fastapi import Path, APIRouter

router = APIRouter(prefix= "/items", tags=["Items"])

@router.get("/")
def items():
    return {
        "ITEM1",
        "ITEM2",
        "ITEM3"
    }
@router.get("/latest/")
def get_latest_item():
    return {
        "latest":{
            "id": "1",
            "name": "latest"
        }
    }
@router.get("/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=555)]):
    return {
        "item": {
            "id": item_id
        }
    }