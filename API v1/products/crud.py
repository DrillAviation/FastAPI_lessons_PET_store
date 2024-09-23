from itertools import product
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Product


async def get_products(session: AsyncSession) -> list[Product]:
    products = []

    return products
