todolist = ["Read Jujutsu Kaisen", "Rewatch The Bear", "Finish NieR: Automata"]

for number, task in enumerate(todolist, 1):
    print(f"{task}. {number}")

print(f"{len(todolist)} tasks left to do.")