def rest_day(fatigue):
    if fatigue <= 3:
        return "You're fine. Go train today!"
    elif fatigue <= 7:
        return "You're good. Just take it nice and easy today."
    else:
        return "Woah. Take the day off and don't hurt yourself."
    
print("June 27th:", rest_day(4))
print("June 28th:", rest_day(5))
print("June 29th:", rest_day(8))
print("June 30th:", rest_day(2))