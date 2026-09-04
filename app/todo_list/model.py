from datetime import datetime

from pydantic import BaseModel, Field

# TODO 리스트 생성 요청
class TodoListCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)

# TODO 리스트 응답
class TodoListResponse(BaseModel):
    id: int
    name: str
    created_at: datetime

# Todo 리스트 저장 모델
class TodoList(BaseModel):
    id: int
    name: str
    created_at: datetime
