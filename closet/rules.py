import statistics

from closet.models import Outfit, Occasion

def has_required_categories(outfit: Outfit):
    categories = {item.category for item in outfit.items}

    valid_combinations = [
        {"dress", "shoes", "accessories"},
        {"top", "bottom", "shoes", "accessories"},
    ]
    return categories in valid_combinations

def is_formal_enough(outfit: Outfit, occasion: Occasion):
    average_formality = statistics.mean(item.formality for item in outfit.items)
    return abs(average_formality - occasion.target_formality) <= 2

def is_comfy_enough(outfit: Outfit, occasion: Occasion):
    average_comfort = statistics.mean(item.comfort for item in outfit.items)
    return average_comfort>=occasion.min_comfort

def is_valid_outfit(outfit: Outfit, occasion: Occasion):
    return (has_required_categories(outfit)
            and is_formal_enough(outfit, occasion)
            and is_comfy_enough(outfit, occasion))