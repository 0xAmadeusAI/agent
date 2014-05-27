from pydantic import BaseModel


class ReplyRequest(BaseModel):
    user_prompt: str
    twitter_username: str
    message: str # might be post, reply, etc etc


class PostRequest(BaseModel):
    user_prompt: str