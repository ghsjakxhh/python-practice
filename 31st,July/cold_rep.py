# made-up data — arcade high scores
scores = [
    "tetris: 4200",
    "pacman: 3100",
    "galaga: 5600",
    "frogger: 2900",
    "digdug: 3800",
]

A = ([data.split(": ")[0], int(data.split(": ")[1])] for data in scores)

highest_score = 0
title = ""

for item in A:
    if item[1] > highest_score:
        highest_score = item[1]
        title = item[0]

print(f"{title}/{highest_score}")