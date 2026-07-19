prices = {"gpu": 800000, "cpu": 450000, "ram": 120000, "ssd": 90000, "case": 60000}



wishlist = ["gpu", "ram", "monitor", "case"]

total = 0

for parts in wishlist:
    try:
        print(f"This {parts} is {prices[parts]}")
        total = total + prices[parts]
    except KeyError as A:
        print(f"Oops! We don't have {A} in the cart.")
    except Exception as B:
        print(f"A {B} was raised.")

print(total)

print(prices.get("headphone", "This isn't in the cart."))