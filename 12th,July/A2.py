backlog = ["NieR Automata", "Resident Evil 2", "Bendy and the Ink Machine", "The Last of Us Part 1", "Little Nightmares 1", "SOMA"]

count = 0

for game in backlog:
    if len(game) > 6:
        count = count + 1

print(f"There are {count} games that have more than 6 characters.")
        