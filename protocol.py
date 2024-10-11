from typing import List

from pydantic import BaseModel, Field


class InsContent(BaseModel):
    type: str = Field(description="帖子类型,比如说视频,文章等等")
    url: str = Field(description="帖子的链接")
    caption: str = Field(default="", description="帖子的具体内容,有可能为空")
    commentsCount: int = Field(description="评论量")
    firstComment: str = Field(description="帖子第一个评论")
    likesCount: int = Field(description="点赞量")
    displayUrl: str = Field(description="帖子的展示图片")
    images: List[str] = Field(
        default_factory=[], description="如果帖子为照片,照片链接,以list形式存储"
    )
    videoUrl: str = Field(default="", description="如果帖子为视频,视频链接")
    timestamp: str = Field(description="UTC时间")
    ownerUsername: str
