from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException, status

from app.tag import tag_repository
from app.todo import todo_repository, todo_tag_repository
from app.todo.model import TodoCreate, TodoResponse, TodoUpdate
from app.todo_list import todo_list_repository


router = APIRouter()


@router.get("/todos", response_model=list[TodoResponse])
def get_todos(tag: str | None = None):
    if tag is None:
        return list(todo_repository.todos.values())

    found_tag = tag_repository.find_by_name(tag)

    if found_tag is None:
        return []

    todo_ids = todo_tag_repository.get_todo_ids(found_tag.id)

    return [
        todo_repository.todos[todo_id]
        for todo_id in sorted(todo_ids)
    ]


@router.post(
    "/todo-lists/{list_id}/todos",
    response_model=TodoResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_todo(list_id: int, request: TodoCreate):
    if list_id not in todo_list_repository.todo_lists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Todo list not found",
        )

    return todo_repository.create(
        todo_list_id=list_id,
        title=request.title,
        description=request.description,
    )


@router.patch("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, request: TodoUpdate):
    if todo_id not in todo_repository.todos:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Todo not found",
        )

    todo = todo_repository.todos[todo_id]

    if request.title is not None:
        todo.title = request.title

    if request.description is not None:
        todo.description = request.description

    return todo


@router.post("/todos/{todo_id}/complete", response_model=TodoResponse)
def complete_todo(todo_id: int):
    if todo_id not in todo_repository.todos:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Todo not found",
        )

    todo = todo_repository.todos[todo_id]
    todo.completed = True
    todo.completed_at = datetime.now(timezone.utc)

    return todo


@router.post("/todos/{todo_id}/uncomplete", response_model=TodoResponse)
def uncomplete_todo(todo_id: int):
    if todo_id not in todo_repository.todos:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Todo not found",
        )

    todo = todo_repository.todos[todo_id]
    todo.completed = False
    todo.completed_at = None

    return todo


@router.delete(
    "/todos/{todo_id}",
    status_code=status.HTTP_200_OK,
)
def delete_todo(todo_id: int):
    if todo_id not in todo_repository.todos:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Todo not found",
        )

    del todo_repository.todos[todo_id]
    todo_tag_repository.remove_by_todo_id(todo_id)

    return {"message": "Todo deleted successfully"}
