screen_time = {"week 1": 23.8, "week 2": 16.5, "week 3": 19.4, "week 4": 27.2}

record = 0

for week, time in screen_time.items():
    if time > record:
        record = time

print(f"My highest screen time was {record} hours")