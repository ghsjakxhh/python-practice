screen_time_avg = {"June 14-21": 5.2, "June 21-28": 5.7, "June 28-July 5": 4}

print("Loading screen time average data...")
try:
    print(screen_time_avg["June 14-21"])
    print(screen_time_avg["June 21-28"])
    print(screen_time_avg["June 28-July 5"])
    print(screen_time_avg.get("June 29th", "Unrecorded data"))
    print(screen_time_avg["June 7-14"])
except KeyError as missing:
    print(f"No data for {missing}. Please come back later...")
except Exception as anything:
    print(f"Something unexpected: {anything}")
print("That's all the data we have.")