shipping = {"seoul": 3500, "busan": 4200, "incheon": 3000, "daegu": 4000}
requested = ["seoul", "jeju", "busan", "incheon", "daegu"]

total = 0

for request in requested:
    try:
        shipping[request]
        total = total + shipping[request]

    except KeyError as A:
        print(f"Sorry but we don't ship from {A}")

    except Exception as B:
        print(f"A {B} was raised")

print(total)

print(shipping.get("jeju", "We apologize for the inconvenience. We don't have that in stock."))