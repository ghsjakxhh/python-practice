exercise = {"A": 10, "B": 20, "C": 5, "D": 45, "E": 15}

title = ""
record = 0

for name, reps in exercise.items():
    if reps > record:
        record = reps
        title = name

print(f"Best: {title} with {record}")