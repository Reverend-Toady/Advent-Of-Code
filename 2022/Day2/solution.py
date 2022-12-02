### PART ONE ###
win = {"A": "Y", "B": "Z", "C": "X"}
draw = {"A": "X", "B": "Y", "C": "Z"}

with open("testcase.txt", "r") as f:
    data = [i.strip().split(" ") for i in f.readlines()]

score = 0
for lhs, rhs in data:
    if draw[lhs] == rhs:
        score += 3

    elif win[lhs] == rhs:
        score += 6

    score += "XYZ".index(rhs) + 1
print(score)

### PART TWO ###
win = {"A": "Y", "B": "Z", "C": "X"}
draw = {"A": "X", "B": "Y", "C": "Z"}
lose = {"A": "Z", "B": "X", "C": "Y"}

with open("testcase.txt", "r") as f:
    data = [i.strip().split(" ") for i in f.readlines()]

score = 0
for lhs, rhs in data:
    if rhs == "Z":  # win
        score += 6 + "XYZ".index(win[lhs]) + 1

    elif rhs == "Y":  # draw
        score += 3 + "XYZ".index(draw[lhs]) + 1

    elif rhs == "X":  # lose
        score += "XYZ".index(lose[lhs]) + 1

print(score)
