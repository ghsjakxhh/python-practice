hours = {"RE4": 20, "DMC5": 15}

try:
    print(hours["NieR: Automata"])
except NameError:
    print("A name doesn't exist")
except Exception as anything:
    print(f"Something unexpected: {anything}")
except KeyError:
    print("A key doesn't exist")
