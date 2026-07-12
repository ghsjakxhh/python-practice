backlog = ["NieR Automata", "Resident Evil 2", "Bendy and the Ink Machine", "The Last of Us Part 1", "Little Nightmares 1", "SOMA"]

record = ""

for title in backlog:
    if len(title) > len(record):
        record = title
    
print(f"The longest game title in the backlog is {record}")