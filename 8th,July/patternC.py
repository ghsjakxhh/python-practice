line = "score:87"

pieces = line.split(":")       # 1. cut → a list
print(pieces)                  # 2. LOOK: where did the number land?
number = int(pieces[1])        # 3. grab by position, convert
print(number + 0)              # 4. the interrogation — dies if step 3 lied