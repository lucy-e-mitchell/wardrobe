from closet.loader import load_wardrobe


wardrobe = load_wardrobe("data/wardrobe.json")

for item in wardrobe:
    print(item.name)