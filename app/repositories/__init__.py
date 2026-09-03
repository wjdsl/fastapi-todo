from app.repositories.comment_repository import CommentRepository
from app.repositories.tag_repository import TagRepository
from app.repositories.todo_list_repository import TodoListRepository
from app.repositories.todo_repository import TodoRepository
from app.repositories.todo_tag_repository import TodoTagRepository


comment_repository = CommentRepository()
tag_repository = TagRepository()
todo_list_repository = TodoListRepository()
todo_repository = TodoRepository()
todo_tag_repository = TodoTagRepository()
