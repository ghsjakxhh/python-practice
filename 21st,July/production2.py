def sales_reps(number):
    while number < 100:
        yield number
        number = number + 10

for reps in sales_reps(70):
    print(reps)