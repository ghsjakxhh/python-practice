hours = {"RE4": 20, "DMC5": 15}
print("Checking library...")
try:
    print(hours["Sekiro"])
except KeyError:
    print("Not in the library.")
print("Done!")