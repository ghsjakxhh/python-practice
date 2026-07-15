def how_urgent(days_left):
    if days_left <= 7:
        return "soon"
    elif days_left <= 3:
        return "URGENT"
    else:
        return "relax"

print("RE7:", how_urgent(2))
print("NieR replay:", how_urgent(7))
print("Backlog cleanup:", how_urgent(30))