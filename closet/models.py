from pydantic import BaseModel
from typing import Literal

Category = Literal[
    "top",
    "bottom",
    "trousers",
    "skirt",
    "shoes",
    "outerwear",
    "dress",
    "accessory",
]

class ClothingItem(BaseModel):
    id: str
    name: str
    category: Category
    colours: list[str]
    formality: int
    warmth: int
    comfort: int
    pattern: str | None = None
    tags: list[str]


class Occasion(BaseModel):
    name: str
    target_formality: int
    min_comfort: int = 1
    preferred_tags: list[str]

class Score(BaseModel):
    name: str
    value: float
    max_value: float
    reason: str | None = None

class Outfit(BaseModel):
    items: list[ClothingItem]
    score: list[Score]
    reasons: list[str]