lines = ["squat: 80", "bench: 60", "deadlift: 120", "row: 70", "press: 45"]

record = 0
exercise = ""

separate = ([line.split(": ")[0], int(line.split(": ")[1])] for line in lines)

#for line in lines:
#    separate = line.split(": ")
#    if int(separate[1]) > record:
#        record = int(separate[1])
#        exercise = separate[0]

for data in separate:
    if data[1] > record:
        record = data[1]
        exercise = data[0]

print(f"The heaviest lift is {exercise} at {record}")