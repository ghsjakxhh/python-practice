birth_rate = ["Niger: 45", "Angola: 42", "DR Congo: 41", "Mali: 40",
              "Chad: 40", "Nigeria: 36", "Ethiopia: 31", "Pakistan: 27",
               "Egypt: 21", "India: 16", "Indonesia: 15", "Mexico: 14",
                "Turkey: 13", "United States: 11", "France: 10", "Brazil: 12",
                 "Germany: 9", "China: 6.4", "Japan: 6", "South Korea: 4.5"]
#Birth rate(per 1,000)

lowest = 1000
lowest_country = ""

clean = (data.split(": ") for data in birth_rate)

for pair in clean:
    if float(pair[1]) < lowest:
        lowest = float(pair[1])
        lowest_country = pair[0]


print(f"The country with the lowest birth rate is {lowest_country}. They have a birth rate of {lowest}")
