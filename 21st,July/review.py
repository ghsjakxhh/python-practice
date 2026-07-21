with open ("study_log.txt", "w") as f:
    f.write("monday: 45\ntuesday: 80\nwednesday: 30\nthursday: 95\nfriday: 60")

with open ("study_log.txt", "r") as g:
    log = g.read()


lines = log.split("\n")
clean = (line.split(": ") for line in lines)

total = 0
record = 0
day =""

adding = (int(data[1]) for data in clean)
for addition in adding:
    total = total + addition

maximum = (int(separate[1]) for separate in clean if int(separate[1]) > record)
for number in maximum:
    if number > record:
        print(number)


print(len(lines))
print(total)
print(day)
