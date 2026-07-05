def verdict(hours):
    if hours <= 30:
        return "Lightweight"
    elif hours < 80:
        return "Meaty"
    else:
        return "Oof. Clear your calendar"
print(verdict(60))

backlog = {"Little Nightmares 1": 70, "Little Nightmares 2": 65,
          "Resident Evil 2": 100, "Welcome to the Game 2": 80,
            "Resident Evil 7 Biohazard": 30, "NieR: Automata": 50}

def time_to_finish(backlog, title):
    return backlog[title]
    
print(time_to_finish(backlog, "Welcome to the Game 2"))