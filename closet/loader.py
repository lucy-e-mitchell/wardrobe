from __future__ import annotations

import json
from pathlib import Path

from closet.models import ClothingItem


def load_wardrobe(path: str | Path) -> list[ClothingItem]:
    path = Path(path)

    with path.open("r") as file:
        data = json.load(file)

    return [
        ClothingItem(**item)
        for item in data
    ]