with open("streak_log.txt", "r") as f:
    log = f.read()

lines = log.split("\n")

count = 0
record = 0

for line in lines:
    if line != "":
        streak = line.split(":")
        days = int(streak[1])
        count = count + 1
        if days > record:
            record = days

print(f"Entries in the log: {count}")
print(f"Highest streak recorded: {record}")