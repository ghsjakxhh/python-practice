with open("streak_log.txt", "a") as f:
    f.write(f"\nToday is {date.today()}. The streak is now {streak}")

with open("streak_log.txt", "r") as g:
    log = g.read()

print(log)