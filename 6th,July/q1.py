def check(hp):
    if hp < 30:
        return "Danger"
    return "Fine"
    print("Checked!")

print(check(25))