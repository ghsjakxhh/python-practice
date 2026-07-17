budget = {
    "food": 320000,
    "transport": 62000,
    "games": 45000,
    "gym": 55000,
}

report = ["transport", "tech", "games", "gym", "food"]

total = 0

for category in report:
    try:
        print(f"{category}: {budget[category]}")
        total = total + budget[category]
    except KeyError as A:
        print(f"We don't have {A} in the budget")
    except Exception as B:
        print(f"A {B} was raised")

print(f"Total spend is {total}")
print(budget.get("clothes", "Not included in the budget"))