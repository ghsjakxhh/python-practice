with open("session_log.txt", "r") as f:
    log = f.read()

lines = log.split("\n")

python = 0
total = 0
most = 0
most_day = ""

for data in lines:
    separate = data.split(" ")
    if separate[1] == "python":
        python = python + 1
    total = total + int(separate[2])
    if int(separate[2]) > most:
        most = int(separate[2])
        delete = separate[0].split(":")
        most_day = delete[0]


print(python)
print(total)
print(most_day)