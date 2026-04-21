from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.models import News
from app.schemas import NewsCreate, NewsOut

router = APIRouter(prefix="/news", tags=["news"])


@router.post("/", response_model=NewsOut)
async def create_news(data: NewsCreate, db: AsyncSession = Depends(get_db)):
    news = News(title=data.title, content=data.content)
    db.add(news)
    await db.commit()
    await db.refresh(news)
    return news


@router.get("/", response_model=list[NewsOut])
async def get_news(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(News))
    return result.scalars().all()

@router.get("/{news_id}", response_model=NewsOut)
async def get_news_by_id(news_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(News).where(News.id == news_id))
    news = result.scalar_one_or_none()

    if news is None:
        raise HTTPException(status_code=404, detail="News not found")

    return news    