days_left = 60

while days_left > 0:
    if days_left > 10:
        mood = "Jesus Christ. Time flies."
    elif days_left > 30:
        mood = "Cortisol level low"
    else:
        mood = "Massive cortisol spike!"

    print(f"{days_left} days left. {mood}")
    days_left = days_left - 1

print("Go to school!!!")