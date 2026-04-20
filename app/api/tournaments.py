from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List

from app.database import get_db
from app.models import Tournament
from app.schemas import TournamentOut

router = APIRouter(prefix="/tournaments", tags=["Tournaments"])


@router.get("/", response_model=List[TournamentOut])
async def get_tournaments(
    skip: int = 0, 
    limit: int = 10, 
    db: AsyncSession = Depends(get_db)
):
    # 1. Формируем запрос (SELECT * FROM tournaments OFFSET skip LIMIT limit)
    query = select(Tournament).offset(skip).limit(limit)
    
    # 2. Выполняем асинхронно
    result = await db.execute(query)
    
    # 3. Достаем объекты из результата
    tournaments = result.scalars().all()
    
    return tournaments