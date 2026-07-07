import datetime

start = datetime.date(2026, 6, 26)
today = datetime.date.today()
streak = (today - start).days

with open("streak_log.txt", "w") as log:
    log.write(f"Today is {today}. Current streak:{streak}\n")

log = open("streak_log.txt", "r")
content = log.read()
log.close()

print(content)