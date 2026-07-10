hours = {"NieR": 42}
try:
    print(hours["DbD"])
except Exception as anything:
    print(f"Broad net caught {anything}")
except KeyError as missing:
    print(f"Missing key: {missing}")