from pydantic import BaseModel

# То, что приходит от Flutter при создании
class TournamentCreate(BaseModel):
    name: str
    location: str | None = None

# То, что мы отдаем назад во Flutter (уже с ID из базы)
class TournamentOut(TournamentCreate):
    id: int

    class Config:
        from_attributes = True # Позволяет Pydantic работать с моделями SQLAlchemy