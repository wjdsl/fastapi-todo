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
