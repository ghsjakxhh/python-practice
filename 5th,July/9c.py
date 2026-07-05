hours = {"RE4": 20, "DMC5": 15}
try:
    print(hours["Sekiro"])
except NameError:
    print("A name doesn't exist")
except KeyError:
    print("A key doesn't exist")
print("Done!")