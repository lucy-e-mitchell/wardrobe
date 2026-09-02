from closet.models import Outfit, Occasion


def formality_score(
    outfit: Outfit,
    occasion: Occasion
) -> float:

    average_formality = sum(
        item.formality
        for item in outfit.items
    ) / len(outfit.items)

    difference = abs(
        average_formality
        - occasion.target_formality
    )

    return max(0, 10 - difference)

def comfort_score(
    outfit: Outfit
) -> float:

    return sum(
        item.comfort
        for item in outfit.items
    ) / len(outfit.items)

def tag_score(
    outfit: Outfit,
    occasion: Occasion
) -> float:

    score = 0

    for item in outfit.items:
        matches = (
            item.tags
            & occasion.preferred_tags
        )

        score += len(matches)

    return score

def score_outfit(
    outfit: Outfit,
    occasion: Occasion
) -> tuple[float, list[str]]:

    score = 0
    reasons = []

    formality = formality_score(
        outfit,
        occasion
    )

    score += formality * 3

    if formality >= 8:
        reasons.append(
            "Good formality match"
        )

    comfort = comfort_score(outfit)

    score += comfort * 2

    if comfort >= 8:
        reasons.append(
            "High comfort"
        )

    tags = tag_score(
        outfit,
        occasion
    )

    score += tags * 2

    return score, reasons