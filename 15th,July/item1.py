with open("session_log.txt", "w") as f:
    f.write("day1: python 40\nday2: rest 0\nday3: python 55\nday4: linux 30")

with open("session_log.txt", "r") as g:
    log = g.read()

lines = log.split("\n")

python_count = 0
total = 0
record= 0
maximum = ""

for data in lines:
    separate = data.split(" ")
    if separate[1] == "python":
        python_count = python_count + 1
    total = total + int(separate[2])
    if int(separate[2]) > record:
        record = int(separate[2])
        day = separate[0].split(":")
        maximum = day[0]
    
print(python_count)
print(total)
print(maximum)