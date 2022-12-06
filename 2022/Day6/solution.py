with open("testcase.txt", "r") as f:
    data = f.read().strip()

### PART ONE ###
for i in range(len(data)):
    items = data[i : i + 4]
    if len(set(items)) == 4:
        print(i + 4)
        break

### PART TWO ###
for i in range(len(data)):
    items = data[i : i + 14]
    if len(set(items)) == 14:
        print(i + 14)
        break
