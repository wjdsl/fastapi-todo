from pydantic import BaseModel, Field


# Tag 생성 및 Todo 연결 요청
class TagCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)


# Tag 응답
class TagResponse(BaseModel):
    id: int
    name: str


# Tag 저장 모델
class Tag(BaseModel):
    id: int
    name: str
