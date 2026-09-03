from fastapi import FastAPI

from app.routers.comment import router as comment_router
from app.routers.tag import router as tag_router
from app.routers.todo import router as todo_router
from app.routers.todo_list import router as todo_list_router

app = FastAPI(title="Todo List API")

app.include_router(todo_list_router)
app.include_router(todo_router)
app.include_router(comment_router)
app.include_router(tag_router)
