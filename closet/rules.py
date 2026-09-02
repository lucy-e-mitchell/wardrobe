from closet.models import ClothingItem, Outfit, Occasion


def has_category(
    outfit: Outfit,
    category: str
) -> bool:

    return any(
        item.category == category
        for item in outfit.items
    )

def has_required_categories(outfit: Outfit) -> bool:

    return (
        has_category(outfit, "top")
        and has_category(outfit, "bottom")
        and has_category(outfit, "shoes")
    )

def has_only_one_bottom(outfit: Outfit) -> bool:

    bottoms = [
        item
        for item in outfit.items
        if item.category == "bottom"
    ]

    return len(bottoms) == 1

def is_formal_enough(
    outfit: Outfit,
    occasion: Occasion
) -> bool:
    if not outfit.items:
        return False

    average_formality = sum(
        item.formality
        for item in outfit.items
    ) / len(outfit.items)

    return average_formality >= occasion.target_formality

def is_valid_outfit(
    outfit: Outfit,
    occasion: Occasion
) -> bool:

    return (
        has_required_categories(outfit)
        and has_only_one_bottom(outfit)
        and is_formal_enough(outfit, occasion)
    )