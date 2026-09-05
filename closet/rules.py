import statistics
from closet.models import Outfit, Occasion, Category

def has_required_categories(outfit: Outfit):
    categories = {item.category for item in outfit.items}

    valid_combinations = [
        {Category.DRESS, Category.SHOES, Category.ACCESSORY},
        {Category.TOP, Category.BOTTOM, Category.SHOES, Category.ACCESSORY},
    ]
    return categories in valid_combinations

def is_formal_enough(outfit: Outfit, occasion: Occasion):
    if not outfit.items:
        return False

    average_formality = statistics.mean(item.formality for item in outfit.items)
    return abs(average_formality - occasion.target_formality) <= 2

def is_comfy_enough(outfit: Outfit, occasion: Occasion):
    if not outfit.items:
        return False
    average_comfort = statistics.mean(item.comfort for item in outfit.items)
    return average_comfort>=occasion.min_comfort

def is_valid_outfit(outfit: Outfit, occasion: Occasion):
    return (has_required_categories(outfit)
            and is_formal_enough(outfit, occasion)
            and is_comfy_enough(outfit, occasion))