backlog = {"Little Nightmares 1": 70, "Little Nightmares 2": 65,
          "Resident Evil 2": 100, "Welcome to the Game 2": 80,
            "Resident Evil 7 Biohazard": 30, "NieR: Automata": 50}

def time_to_finish(backlog, title):
    return backlog[title]


def verdict(hours):
    if hours <= 30:
        return "Lightweight"
    elif hours < 80:
        return "Meaty"
    else:
        return "Oof. Clear your calendar"
    
total = 0

print("Your backlog:")
for game, time in backlog.items():
    print(f"{game}: {time_to_finish(backlog, game)} - {verdict(time)}")
    total = total + time
print(f"Total: {total} - {verdict(total)}")
try:
    print(backlog["Elden Ring"])
except KeyError as missing:
    print(f"No data for {missing}")