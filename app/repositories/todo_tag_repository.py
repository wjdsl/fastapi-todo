# Todo와 Tag의 다대다 연결 관계 저장소 관리 클래스
class TodoTagRepository:
    def __init__(self):
        self.todo_tags: set[tuple[int, int]] = set()

    def add(self, todo_id: int, tag_id: int) -> None:
        self.todo_tags.add((todo_id, tag_id))

    def get_tag_ids(self, todo_id: int) -> list[int]:
        return [
            tag_id
            for connected_todo_id, tag_id in self.todo_tags
            if connected_todo_id == todo_id
        ]

    def get_todo_ids(self, tag_id: int) -> list[int]:
        return [
            todo_id
            for todo_id, connected_tag_id in self.todo_tags
            if connected_tag_id == tag_id
        ]

    def remove_by_todo_id(self, todo_id: int) -> None:
        self.todo_tags = {
            relation
            for relation in self.todo_tags
            if relation[0] != todo_id
        }
