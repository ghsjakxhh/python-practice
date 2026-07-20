with open("workout_log.txt", "w") as f:
    f.write("day1: sprint 40\nday2: rest 0\nday3: gym 55\nday4: rest 0\nday5: sprint 45\nday6: gym 60")
# made-up data

with open("workout_log.txt", "r") as g:
    log = g.read()

lines = log.split("\n")

non_rest = 0
total = 0
record = 0
day = ""

workout = [line for line in lines if line.split(" ")[1] != "rest"]
minutes = [int(session.split(" ")[2]) for session in workout]

for work in workout:
    separate = work.split(" ")
    time = int((separate[2]))
    if time > record:
        record = time
        no_colon = separate[0].split(":")
        day = no_colon[0]

for time in minutes:
    total = total + time


print(len(workout))
print(total)
print(day)