from fastapi import APIRouter, HTTPException, status

from app.models.comment import CommentCreate, CommentResponse
from app.repositories import comment_repository, todo_repository


router = APIRouter()


@router.post(
    "/todos/{todo_id}/comments",
    response_model=CommentResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_comment(todo_id: int, request: CommentCreate):
    if todo_id not in todo_repository.todos:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Todo not found",
        )

    return comment_repository.create(
        todo_id=todo_id,
        content=request.content,
    )


@router.get(
    "/todos/{todo_id}/comments",
    response_model=list[CommentResponse],
)
def get_comments(todo_id: int):
    if todo_id not in todo_repository.todos:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Todo not found",
        )

    return comment_repository.find_by_todo_id(todo_id)
