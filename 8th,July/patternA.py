snacks = {"chips": 1500, "cola": 2000, "ramen": 1200}   # made-up data

count = 0                      # 1. seed, BEFORE the loop
for name, price in snacks.items():   # 2. loop the dict
    count = count + 1          # 3. feed: +1 every lap
print(f"Items: {count}")       # 4. report, AFTER the loop