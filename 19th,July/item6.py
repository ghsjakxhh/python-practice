screen_time = ["7 hours", "2 hours", "", "11 hours", ""]

clean = [time for time in screen_time if time != ""]
screen_time_integer = [int(time.split(" ")[0]) for time in screen_time if time != ""]

print(clean)
print(screen_time_integer)