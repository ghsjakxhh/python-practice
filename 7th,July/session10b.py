import datetime

today = datetime.date.today()
start = datetime.date(2026, 6, 26)
streak = today - start.days

log = open("streak_log.txt", "w")
log.write(f"Day {streak} of the streak.\n")
log.write("Session 10: files and datetime.\n")
log.close()

print("Written.")

log = open("streak_log.txt", "r")
content = log.read()
log.close()

print(content)

