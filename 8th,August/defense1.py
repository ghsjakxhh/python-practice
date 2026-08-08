with open ("trail_road.txt", "w") as f:
    f.write("2026-03-01: trail 8.2\n2026-03-02: road 5.0\n2026-03-04: trail 12.6\n2026-03-05: trail 6.1\n2026-03-07: road 9.4\n2026-03-09: trail 12.6")

with open ("trail_road.txt", "r") as g:
    log = g.read()

lines = log.split("\n")

trail_count = 0
total_trail = 0
longest_trail_date = ""
longest_trail = 0

for line in lines:
    line.split(" ")
    if line.split(" ")[1] == "trail":
        trail_count = trail_count + 1
        total_trail = total_trail + float(line.split(" ")[2])
        if float(line.split(" ")[2]) >= longest_trail:
            longest_trail = float(line.split(" ")[2])
            longest_trail_date = line.split(" ")[0].split(":")[0]
    

print(trail_count)
print(total_trail)
print(longest_trail_date)