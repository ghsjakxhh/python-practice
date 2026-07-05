hours = {"RE4": 20, "DMC5": 15}
print(hours.get("RE4"))
print(hours.get("Sekiro"))
print(hours.get("Sekiro", 0))
print("Done!")
print(hours["Sekiro"])