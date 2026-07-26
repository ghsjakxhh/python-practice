with open ("expense_log.txt", "w") as f:
    f.write("day1: food 8000\nday2: transport 3000\nday3: food 12000\nday4: study 15000\nday5: food 6500")

with open ("expense_log.txt", "r") as g:
    log = g.read()

lines = log.split("\n")

food_count = 0
total_spend = 0
highest_expense = 0
highest_expense_day = ""

for line in lines:
    separate = line.split(" ")
    if separate[1] == "food":
        food_count = food_count + 1
    total_spend = total_spend + int(separate[2])
    if int(separate[2]) > highest_expense:
        highest_expense = int(separate[2])
        no_colon = separate[0].split(":")
        highest_expense_day = no_colon[0]


print(food_count)
print(total_spend)
print(highest_expense_day)