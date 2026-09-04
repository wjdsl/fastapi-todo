from fastapi import APIRouter, HTTPException, status

from app.tag import tag_repository
from app.tag.model import TagCreate, TagResponse
from app.todo import todo_repository, todo_tag_repository


router = APIRouter()


@router.post(
    "/todos/{todo_id}/tags",
    response_model=TagResponse,
    status_code=status.HTTP_201_CREATED,
)
def add_tag(todo_id: int, request: TagCreate):
    if not todo_repository.exists(todo_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Todo not found",
        )

    tag = tag_repository.find_by_name(request.name)

    if tag is None:
        tag = tag_repository.create(name=request.name)

    todo_tag_repository.add(todo_id, tag.id)

    return tag


@router.get(
    "/todos/{todo_id}/tags",
    response_model=list[TagResponse],
)
def get_tags(todo_id: int):
    if not todo_repository.exists(todo_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Todo not found",
        )

    tag_ids = todo_tag_repository.get_tag_ids(todo_id)

    return tag_repository.find_by_ids(sorted(tag_ids))
