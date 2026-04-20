from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean, DateTime
from datetime import datetime
from .database import Base

class Tournament(Base):
    __tablename__ = "tournaments"
    
    # primary_key=True автоматически делает это поле SERIAL (автоинкремент)
    id: Mapped[int] = mapped_column(primary_key=True)
    
    name: Mapped[str] = mapped_column(String(255))
    location: Mapped[str | None] = mapped_column(String(255))
    
    # По умолчанию турнир активен
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    
    # Дата создания (сервер сам проставит время)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)