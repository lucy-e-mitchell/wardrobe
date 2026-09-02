from __future__ import annotations

from pydantic import BaseModel
from typing import Literal


Category = Literal[
    "top",
    "bottom",
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

    tags: set[str] = set()


class Occasion(BaseModel):
    name: str

    target_formality: int
    minimum_comfort: int = 1

    preferred_tags: set[str] = set()


class Outfit(BaseModel):
    items: list[ClothingItem]


class OutfitSuggestion(BaseModel):
    outfit: Outfit
    score: float
    reasons: list[str]