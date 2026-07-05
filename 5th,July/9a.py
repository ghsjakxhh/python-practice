hours = {"RE4": 20, "DMC5": 15}
print("Checking...")
try:
    print(hours["Sekiro"])
except KeyError as missing:
    print(f"Not in the library: {missing}")
print("Done!")