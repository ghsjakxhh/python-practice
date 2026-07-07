import datetime

today = datetime.date.today()
print(today)

start = datetime.date(2026, 6, 26)
streak = today - start

print(streak)
print(streak.days)
print(streak.days + 5)