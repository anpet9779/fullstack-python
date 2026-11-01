from typing import List, Optional
from pydantic import BaseModel


class Comment(BaseModel):
    id: int
    text: str
    replies: Optional[List["Comment"]] = None  # Self-referencing field

Comment.model_rebuild()

comment = Comment(id=1, text="This is a comment")
comment.replies = [
    Comment(id=2, text="This is a reply"),
    Comment(id=3, text="This is a reply", replies=[
        Comment(id=4, text="This is a nested reply"),
    ])
]


print(comment)