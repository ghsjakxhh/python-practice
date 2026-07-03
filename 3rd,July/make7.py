PC_Build = { "GPU": 200, "CPU": 75, "Monitor": 65, "RAM": 100}

print(PC_Build["Monitor"])

PC_Build["Monitor"] = PC_Build["Monitor"] - 15
print(PC_Build["Monitor"])

PC_Build["Headphone"] = 50

print(len(PC_Build))