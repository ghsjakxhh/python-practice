sprint = {"07-01": 30, "07-02": 40, "07-03": 10, "07-04": 70, "07-05": 50}

date = ""
record = 0

for key, distance in sprint.items():
    if distance > record:
        record = distance
        date = key

print(date)

