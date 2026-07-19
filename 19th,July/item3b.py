import datetime

start = datetime.date(2026, 7, 18)
today = datetime.date.today()
days = (today - start).days

print(today)
print(days)