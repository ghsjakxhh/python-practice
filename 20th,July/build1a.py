for line in lines:
    separate = line.split(" ")
    if separate[1] != "rest":
        non_rest = non_rest + 1
        total = total + int(separate[2])
    if int(separate[2]) > longest:
        longest = int(separate[2])
        no_colon = separate[0].split(":")
        day = no_colon[0]
