# made-up data — daily reading log (pages)
log = [
    "monday: 32",
    "tuesday: 41",
    "wednesday: n/a",
    "thursday: 55",
    "friday: 28",
]

splitting_log = [data.split(": ") for data in log]

count = 0
total = 0
most_pages = 0
most_pages_day = ""

for data in splitting_log:
    try:
        total = total + int(data[1])
        count = count + 1
        if int(data[1]) > most_pages:
            most_pages_day = data[0]
            most_pages = int(data[1])
    except ValueError as A:
        print(f"A ValueError was raised because of {A}")

print(f"{count} valid days, {total} total, {most_pages_day}/{most_pages}")