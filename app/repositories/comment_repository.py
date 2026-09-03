from datetime import datetime, timezone

from app.models.comment import Comment


# Comment 저장소 관리 클래스
class CommentRepository:
    def __init__(self):
        self.comments: dict[int, Comment] = {}
        self.next_comment_id = 1

    def create(self, todo_id: int, content: str) -> Comment:
        comment_id = self.next_comment_id
        comment = Comment(
            id=comment_id,
            todo_id=todo_id,
            content=content,
            created_at=datetime.now(timezone.utc),
        )
        self.comments[comment_id] = comment
        self.next_comment_id += 1

        return comment

    def find_by_todo_id(self, todo_id: int) -> list[Comment]:
        return [
            comment
            for comment in self.comments.values()
            if comment.todo_id == todo_id
        ]
