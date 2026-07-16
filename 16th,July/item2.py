hours = {
    "Silent Hill 2": 30,
    "NieR: Automata": 45,
    "Dead by Daylight": 120,
    "Resident Evil 4": 25,
}

report = ["Silent Hill 2", "NieR: Automata", "Bloodborne", "Resident Evil 4", "Dead by Daylight"]

total = 0

for title in report:
    try:
        print(f"{title}: {hours[title]} hours")
        total = total + hours[title]
    except KeyError as A:
        print(f"There is no {A} in the log")
    except Exception as anything:
        print(f"A {anything} was raised")


print(f"Total playtime: {total}")

print(hours.get("NieR Replicant", "Game Not Found"))

