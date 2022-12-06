crates = [
    ["D", "L", "V", "T", "M", "H", "F"],
    ["H", "Q", "G", "J", "C", "T", "N", "P"],
    ["R", "S", "D", "M", "P", "H"],
    ["L", "B", "V", "F"],
    ["N", "H", "G", "L", "Q"],
    ["W", "B", "D", "G", "R", "M", "P"],
    ["G", "M", "N", "R", "C", "H", "L", "Q"],
    ["C", "L", "W"],
    ["R", "D", "L", "Q", "J", "Z", "M", "T"]
]

with open("instructions.txt", "r") as f:
    data = [(i.split(" ")[1], i.split(" ")[3], i.split(" ")[5]) for i in f.read().splitlines()]

### PART ONE ### 

crates = [i[::-1] for i in crates]

for items, start, end in data:
    items, start, end = [int(i) for i in [items, start, end]]

    for i in range(items):
        item = crates[start - 1].pop(0)
        crates[end - 1].insert(0, item)

print("".join([i[0] for i in crates]))

### PART TWO ### 

crates = [i[::-1] for i in crates]

for items, start, end in data:
    items, start, end = [int(i) for i in [items, start, end]]

    stuff = crates[start - 1][:items]
    del crates[start - 1][:items]
    crates[end - 1] = stuff + crates[end - 1]

print("".join([i[0] for i in crates]))