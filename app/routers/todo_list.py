from fastapi import APIRouter, status

from app.models.todo_list import TodoListCreate, TodoListResponse
from app.repositories import todo_list_repository


router = APIRouter()


@router.post(
    "/todo-lists",
    response_model=TodoListResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_todo_list(request: TodoListCreate):
    return todo_list_repository.create(name=request.name)
