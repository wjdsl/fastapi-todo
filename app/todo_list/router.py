from fastapi import APIRouter, status

from app.todo_list import todo_list_repository
from app.todo_list.model import TodoListCreate, TodoListResponse


router = APIRouter()


@router.post(
    "/todo-lists",
    response_model=TodoListResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_todo_list(request: TodoListCreate):
    return todo_list_repository.create(name=request.name)
