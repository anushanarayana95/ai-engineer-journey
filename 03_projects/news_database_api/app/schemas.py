from pydantic import BaseModel

class NewsItem(BaseModel):
    title: str
    source: str
    published: str