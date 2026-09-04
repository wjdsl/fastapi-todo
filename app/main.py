from fastapi import FastAPI

from app.comment.router import router as comment_router
from app.tag.router import router as tag_router
from app.todo.router import router as todo_router
from app.todo_list.router import router as todo_list_router

app = FastAPI(title="Todo List API")

app.include_router(todo_list_router)
app.include_router(todo_router)
app.include_router(comment_router)
app.include_router(tag_router)
