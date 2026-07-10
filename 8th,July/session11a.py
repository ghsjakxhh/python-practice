report = "day10:15\nday11:16\nday12:17\n"

lines = report.split("\n")
print(lines)
print(len(lines))

lines.append("day13:18")
print(len(lines))