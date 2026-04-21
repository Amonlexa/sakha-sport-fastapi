from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.api.news import router as news_router

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(news_router)


@app.get("/")
async def root():
    return {"message": "Sakha Sport API"}