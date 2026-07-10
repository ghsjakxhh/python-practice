snacks = {"chips": 1500, "cola": 2000, "ramen": 1200}   # made-up data

record = 0                     # 1. seed that LOSES the first comparison
for name, price in snacks.items():
    if price > record:         # 2. does this lap beat the record?
        record = price         # 3. if yes: overwrite
print(f"Most expensive: {record}")   # 4. report after