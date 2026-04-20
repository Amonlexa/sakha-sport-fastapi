from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .database import get_db
from .models import Tournament
from .schemas import TournamentCreate, TournamentOut
from app.api.tournaments import router as tournament_router
app = FastAPI()
app.include_router(tournament_router)
@app.post("/tournaments", response_model=TournamentOut)
async def create_tournament(
    data: TournamentCreate, 
    db: AsyncSession = Depends(get_db)
):
    new_tournament = Tournament(
        name=data.name, 
        location=data.location
    )
    
    db.add(new_tournament)
    await db.commit()
    await db.refresh(new_tournament)
    
    return new_tournament