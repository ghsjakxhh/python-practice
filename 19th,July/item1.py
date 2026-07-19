with open("training_log.txt", "w") as f:
    f.write("day1: sprint 40\nday2: gym 50\nday3: sprint 35\nday4: sprint 60\nday5: gym 20")

with open("training_log.txt", "r") as g:
    log = g.read()

lines = log.split("\n")

sprint = 0
total = 0
longest = 0
day = ""

for line in lines:
    three_data = line.split(" ")
    if three_data[1] == "sprint":
        sprint = sprint + 1
    total = total + int(three_data[2])
    if int(three_data[2]) > longest:
        longest = int(three_data[2])
        no_colon = three_data[0].split(":")
        day = no_colon[0]

print(sprint)
print(total)
print(day)