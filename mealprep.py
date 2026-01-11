from collections import defaultdict
from pathlib import Path
from datetime import datetime

# -------- CONFIG --------

MEAL_PLAN = {
    "Monday - Pasta": {
        "pasta (g)": 200,
        "tomato sauce (ml)": 150,
        "olive oil (tbsp)": 1,
        "garlic (cloves)": 2
    },
    "Tuesday - Omelette": {
        "eggs": 3,
        "cheese (g)": 50,
        "milk (ml)": 30
    },
    "Wednesday - Salad": {
        "lettuce (head)": 1,
        "tomato": 2,
        "olive oil (tbsp)": 1
    }
}

PANTRY = {
    "pasta (g)": 100,
    "olive oil (tbsp)": 3,
    "eggs": 2,
    "milk (ml)": 200
}

OUTPUT_FILE = Path("grocery_list.txt")

# ------------------------

def calculate_needed_ingredients(meal_plan):
    total_needed = defaultdict(int)
    for meal, ingredients in meal_plan.items():
        for ingredient, amount in ingredients.items():
            total_needed[ingredient] += amount
    return total_needed

def generate_grocery_list(total_needed, pantry):
    grocery_list = {}
    for ingredient, needed_qty in total_needed.items():
        pantry_qty = pantry.get(ingredient, 0)
        if pantry_qty < needed_qty:
            grocery_list[ingredient] = needed_qty - pantry_qty
    return grocery_list

def save_grocery_list(grocery_list):
    date = datetime.now().strftime("%Y-%m-%d")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(f"Grocery List - {date}\n")
        file.write("-" * 30 + "\n")
        for item, qty in grocery_list.items():
            file.write(f"- {item}: {qty}\n")

def main():
    print("\n🛒 Grocery List Generator\n" + "-" * 30)

    total_needed = calculate_needed_ingredients(MEAL_PLAN)
    grocery_list = generate_grocery_list(total_needed, PANTRY)

    if grocery_list:
        print("\nItems to buy:")
        for item, qty in grocery_list.items():
            print(f"  - {item}: {qty}")
        save_grocery_list(grocery_list)
        print(f"\n📂 Saved to {OUTPUT_FILE.resolve()}")
    else:
        print("\n✅ Your pantry is fully stocked!")

if __name__ == "__main__":
    main()
    journal_entry = input("\n🖊️ Your Entry:\n")