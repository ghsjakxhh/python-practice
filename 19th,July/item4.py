# P1
names = ["ryu", "ken", "akuma"]
loud = [n.upper() for n in names]
print(loud)

# P2
streaks = ["day1: 20", "day2: 21", "day3: 22"]
nums = [line.split(": ")[1] for line in streaks]
print(nums)

# P3 — trap. What does this print, and is anything wrong with it?
values = [10, 20, 30]
result = [v + 5 for v in values]
print(result[3])

