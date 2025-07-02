# nutrition.py

if __name__ == "__main__":
    dict1 = { \
        "apple":130 , "avocado":50 , "banana":110 , "cantaloupe":50 , \
        "grapefruit":60 , "grapes":90 , "honeydew melon":50 , "kiwifruit":90 , \
        "lemon":15 , "lime":20 , "nectarine":60 , "orange":80 , \
        "peach":60 , "pear":100 , "pineapple":50 , "plums":70 , \
        "strawberries":50 , "sweet cherries":100 , "tangerine":50 , \
        "water melon":80 \
    }

    fruit = input("Item: ").lower()
    calories = int(dict1.get(fruit, -1))
    if calories > 0 :
        print(f"Calories: {calories}")
