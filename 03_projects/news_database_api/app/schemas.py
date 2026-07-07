from pydantic import BaseModel

class NewsItem(BaseModel):
    title: str
    source: str
    published: str


class MessageResponse(BaseModel):
    message: str


class NewsResponse(BaseModel):
    total: int
    news: list[NewsItem]