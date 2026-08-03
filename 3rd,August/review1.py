# fake data — invented for this rep
sightings = ["magpie", "cat", "magpie", "pigeon", "cat", "magpie", "heron", "pigeon", "magpie"]

tally = {}

for animal in sightings:
    tally[animal] = tally.get(animal, 0) + 1

for animal in tally:
    print(f"{animal}:{tally[animal]}")