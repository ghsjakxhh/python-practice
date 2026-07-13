playtime = {"The Last of Us": 80, "Resident Evil 7": 100, "Welcome to the Game 2": 2, "Resident Evil 2": 20, "Bendy and the Ink Machine": 45}

count = 0

for title, time in playtime.items():
    if time > 40:
        count = count + 1

print(count)