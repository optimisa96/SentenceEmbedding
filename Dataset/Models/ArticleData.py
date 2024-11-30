# Predetermined categories will be:
# Technology
# Sport
# Politics
# Health
# Culture
from enum import Enum

class ArticleCategory(Enum):
    TECHNOLOGY = 0
    SPORT = 1
    POLITICS = 2
    HEALTH = 3
    CULTURE = 4

class ArticleData:
    def __init__(self, source, category, heading, summary, text, img_url):
        self.source = source
        self.category = category
        self.heading = heading
        self.summary = summary
        self.text = text
        self.img_url = img_url

    def to_dict(self) -> dict:
        return {
            "source": self.source,
            "category": self.category,
            "heading": self.heading,
            "summary": self.summary,
            "text": self.text,
            "img_url": self.img_url,
        }
    
    def from_dict(source_dict: dict):
        return ArticleData(source_dict["source"],
                           source_dict["category"],
                           source_dict["heading"],
                           source_dict["summary"],
                           source_dict["text"],
                           source_dict["img_url"])
    

