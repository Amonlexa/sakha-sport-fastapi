from pydantic import BaseModel


class NewsCreate(BaseModel):
    title: str
    content: str


class NewsOut(BaseModel):
    id: int
    title: str
    content: str

    model_config = {
        "from_attributes": True
    }