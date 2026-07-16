with open("session_log.txt", "w") as f:
    f.write("day1: Python 40\nday2: Linux 25\nday3: Python 20\nday4: CAD 50")
    
with open("session_log.txt", "r") as g:
    log = g.read()

lines = log.split("\n")

python_count = 0
total = 0
record = 0
day = ""

for line in lines:
    data = line.split(" ")
    if data[1] == "Python":
        python_count = python_count + 1
    total = total + int(data[2])
    if int(data[2])  > record:
        record = int(data[2])
        most = data[0].split(":")
        day = most[0]

print(python_count)
print(total)
print(day)