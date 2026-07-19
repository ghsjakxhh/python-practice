from datetime import date

start = date(2026, 6, 26)
today = date.today()
gap = today - start
streak = gap.days + 1

with open("streak_log.txt", "r") as h:
    log = h.read()
lines = log.split("\n")
print(lines)


line_count = 0

for line in lines:
    line_count = line_count + 1

separate = lines[line_count - 1].split(" ")

if int(separate[7]) < streak:
    with open("streak_log.txt", "a") as f:
        f.write(f"\nToday is {today}. The streak is now {streak}")


with open("streak_log.txt", "r") as g:
    log = g.read()

print(log)