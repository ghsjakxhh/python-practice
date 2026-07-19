from datetime import date

start = date(2026, 6, 26)
today = date.today()

gap = today - start
gap_days = gap.days

print(start)
print(today)

print(gap)
print(f"It's been {gap_days} days since I started learning CS.")
print(f"Today is {date.today()}")