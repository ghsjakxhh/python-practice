with open("training_log.txt", "r") as f:
    content = f.read()

lines = content.split("\n")

record = 0
total = 0
sprint_sessions = 0
best = ""

for session in lines:
    if session != "":
        meaning = session
        three = meaning.split("|")
        rep = int(three[2])
        total = rep + total
        if rep > record:
            record = rep
            best = three[0]
        if three[1] == "sprint":
            sprint_sessions = sprint_sessions + 1
        


print(f"Sprint sessions: {sprint_sessions}")
print(f"Total reps: {total}")
print(f"Best day: {best}")



