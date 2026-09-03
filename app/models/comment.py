from datetime import datetime

from pydantic import BaseModel, Field


# Comment 생성 요청
class CommentCreate(BaseModel):
    content: str = Field(min_length=1)


# Comment 응답
class CommentResponse(BaseModel):
    id: int
    todo_id: int
    content: str
    created_at: datetime


# Comment 저장 모델
class Comment(BaseModel):
    id: int
    todo_id: int
    content: str
    created_at: datetime
