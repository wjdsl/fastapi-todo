from datetime import datetime, timezone

from app.models.todo_list import TodoList


# Todo 리스트 저장소 관리 클래스
class TodoListRepository:
    def __init__(self):
        self.todo_lists: dict[int, TodoList] = {}
        self.next_todo_list_id = 1

    def create(self, name: str) -> TodoList:
        todo_list_id = self.next_todo_list_id
        todo_list = TodoList(
            id=todo_list_id,
            name=name,
            created_at=datetime.now(timezone.utc),
        )
        self.todo_lists[todo_list_id] = todo_list
        self.next_todo_list_id += 1

        return todo_list
