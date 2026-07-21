def countdown(start):
    while start > 0:
        yield start
        start = start - 1
    print("Liftoff!")

for n in countdown(3):
    print(n)