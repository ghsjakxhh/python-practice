pc_build = {"CPU": 350000, "GPU": 2500000, "headphone": 300000, "monitor": 450000}

record = 0

for stuff, price in pc_build.items():
    if price > record:
        record = price

print(f"The most expensive item costs {record} won.")