todolist = ["Read Jujutsu Kaisen", "Rewatch the Bear", "Finish NieR: Automata"]

for task, counter in enumerate(todolist, 10):
    print(f"{counter}. {task}")

print(f"{len(todolist)} tasks left to do.")