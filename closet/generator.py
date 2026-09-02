from itertools import product

from closet.models import Outfit
from closet.rules import is_valid_outfit
from closet.scoring import score_outfit


def generate_outfits(
    wardrobe,
    occasion,
    limit=5
):

    tops = [
        item for item in wardrobe
        if item.category == "top"
    ]

    bottoms = [
        item for item in wardrobe
        if item.category == "bottom"
    ]

    shoes = [
        item for item in wardrobe
        if item.category == "shoes"
    ]

    suggestions = []

    for top, bottom, shoe in product(
        tops,
        bottoms,
        shoes
    ):

        outfit = Outfit(
            items=[
                top,
                bottom,
                shoe
            ]
        )

        if not is_valid_outfit(
            outfit,
            occasion
        ):
            continue

        score, reasons = score_outfit(
            outfit,
            occasion
        )

        suggestions.append(
            {
                "outfit": outfit,
                "score": score,
                "reasons": reasons
            }
        )

    suggestions.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return suggestions[:limit]