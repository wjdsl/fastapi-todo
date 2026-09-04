from datetime import datetime, timezone
from typing import Optional

from app.todo.model import Todo


# Todo 저장소 관리 클래스
class TodoRepository:
    def __init__(self):
        self.todos: dict[int, Todo] = {}
        self.next_todo_id = 1

    def create(
        self,
        todo_list_id: int,
        title: str,
        description: Optional[str],
    ) -> Todo:
        todo_id = self.next_todo_id
        todo = Todo(
            id=todo_id,
            todo_list_id=todo_list_id,
            title=title,
            description=description,
            completed=False,
            completed_at=None,
        )
        self.todos[todo_id] = todo
        self.next_todo_id += 1

        return todo

    def find_all(self) -> list[Todo]:
        return list(self.todos.values())

    def find_by_ids(self, todo_ids: list[int]) -> list[Todo]:
        return [self.todos[todo_id] for todo_id in todo_ids]

    def exists(self, todo_id: int) -> bool:
        return todo_id in self.todos

    def update(
        self,
        todo_id: int,
        title: Optional[str],
        description: Optional[str],
    ) -> Optional[Todo]:
        todo = self.todos.get(todo_id)

        if todo is None:
            return None

        if title is not None:
            todo.title = title

        if description is not None:
            todo.description = description

        return todo

    def complete(self, todo_id: int) -> Optional[Todo]:
        todo = self.todos.get(todo_id)

        if todo is None:
            return None

        todo.completed = True
        todo.completed_at = datetime.now(timezone.utc)

        return todo

    def uncomplete(self, todo_id: int) -> Optional[Todo]:
        todo = self.todos.get(todo_id)

        if todo is None:
            return None

        todo.completed = False
        todo.completed_at = None

        return todo

    def delete(self, todo_id: int) -> bool:
        if todo_id not in self.todos:
            return False

        del self.todos[todo_id]

        return True
