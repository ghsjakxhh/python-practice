code_level = 0

while code_level <= 100:
    if code_level <= 15:
        status = "Script kiddie."
    elif code_level <= 50:
        status = "Maker"
    elif code_level <= 80:
        status = "Competent Builder"
    else:
        status = "God Level Creator"
    print(f"Code level: {status}. Go sharpen your coding skills with Claude.")
    code_level = code_level + 1

print("Congratulations. You can now build and create whatever you want. Go change the world!")