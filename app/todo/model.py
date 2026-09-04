from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

# TODO 생성 요청
class TodoCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: Optional[str] = None

# TODO 응답
class TodoResponse(BaseModel):
    id: int
    todo_list_id: int
    title: str
    description: Optional[str] = None
    completed: bool
    completed_at: Optional[datetime] = None

# TODO 수정 요청
class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

# Todo 저장 모델
class Todo(BaseModel):
    id: int
    todo_list_id: int
    title: str
    description: Optional[str] = None
    completed: bool
    completed_at: Optional[datetime] = None
