# made-up data — workout log
workouts = [
    "run", "swim", "run", "rest", "lift",
    "run", "swim", "rest", "lift", "run",
]

tally = {}

for workout in workouts:
    if workout != "rest":
        tally[workout] = tally.get(workout, 0) + 1

work_sessions = 0
most_frequent = 0
most_frequent_name = ""

for data in tally:
    work_sessions = work_sessions + tally[data]
    if tally[data] > most_frequent:
        most_frequent_name = data
        most_frequent = tally[data]

print(f"{work_sessions} sessions, {most_frequent_name}/{most_frequent}")