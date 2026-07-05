screen_time_avg = {"May 24-30": 6.2, "May 31-June 6": 5.3,
                    "June 7-13": 4.8, "June 14-20": 3.5, "June 21-27": 3.3}

total = 0

for date, time in screen_time_avg.items():
    print(f"{date}: {time} hours")
    if time <= 3.5:
        print("Light")
    elif time <= 5:
        print("Medium")
    else:
        print("Heavy")
    total = total + time
try:
    print(screen_time_avg["April 3-9"])
except KeyError as missing:
    print(f"Sorry. We couldn't find your {missing} data.")
print(f"The average screen time is {total / len(screen_time_avg)}" )