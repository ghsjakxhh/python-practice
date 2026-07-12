with open("streak_log.txt", "r") as f:
    log = f.read()

lines = log.split("\n")

count = 0
record = 0

for line in lines:
    if line != "":
        count = count + 1
        days = line.split(":")
        days = days[1]
        number = int(days)
        if number > record:
            record = number


print(f"There are currently {count} entries.")
print(f"The highest streak is {record}.")