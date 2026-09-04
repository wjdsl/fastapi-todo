from typing import Optional

from app.tag.model import Tag


# Tag 저장소 관리 클래스
class TagRepository:
    def __init__(self):
        self.tags: dict[int, Tag] = {}
        self.next_tag_id = 1

    def find_by_name(self, name: str) -> Optional[Tag]:
        return next(
            (tag for tag in self.tags.values() if tag.name == name),
            None,
        )

    def find_by_ids(self, tag_ids: list[int]) -> list[Tag]:
        return [self.tags[tag_id] for tag_id in tag_ids]

    def create(self, name: str) -> Tag:
        tag_id = self.next_tag_id
        tag = Tag(id=tag_id, name=name)
        self.tags[tag_id] = tag
        self.next_tag_id += 1

        return tag
