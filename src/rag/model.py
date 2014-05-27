from pydantic import BaseModel


class TweetContent(BaseModel):
    author_id: str # cause, author might change the username
    author_username: str
    content: str
    date_created: str
    date_updated: str | None # post/reply might be updated