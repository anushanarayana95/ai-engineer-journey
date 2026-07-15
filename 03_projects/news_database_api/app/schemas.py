from pydantic import BaseModel

class NewsItem(BaseModel):
    title: str
    source: str
    published: str


class NewsResponse(BaseModel):
    total: int
    news: list


class MessageResponse(BaseModel):
    message: str


class SearchRequest(BaseModel):
    keyword: str | None = None
    source: str | None = None
    date: str | None = None
class NewsResponse(BaseModel):
    page: int
    limit: int
    total: int
    pages: int
    news: list[NewsItem]