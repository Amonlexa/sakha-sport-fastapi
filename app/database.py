from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
import os

load_dotenv()
USER = os.getenv("USER") 
DB_NAME = "sakha_sport_db"
DB_HOST = "localhost"
DATABASE_URL = f"postgresql+asyncpg://{USER}@{DB_HOST}:5432/{DB_NAME}"

# echo=True заставит FastAPI выводить все SQL запросы в консоль (удобно для обучения)
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

async def get_db():
    async with SessionLocal() as session:
        yield session