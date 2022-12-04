### PART ONE ###
with open("testcase.txt", "r") as f:
    data = [i.split(",") for i in f.read().splitlines()]

ans1 = 0
for l, r in data:
    l1, l2 = l.split("-")
    r1, r2 = r.split("-")

    if int(r1) <= int(l1) <= int(r2) or int(l1) <= int(l2) <= int(r2):
        ans1 += 1
    elif int(l1) <= int(r1) <= int(l2) or int(r1) <= int(r2) <= int(l2):
        ans1 += 1

print(f"{ans1=}")

### PART TWO ### 
with open("testcase.txt", "r") as f:
    data = [i.split(",") for i in f.read().splitlines()]

ans2 = 0
for l, r in data:
    l1, l2 = l.split("-")
    r1, r2 = r.split("-")

    if int(l1) <= int(r1) <= int(l2) or int(l1) <= int(r2) <= int(l2):
        ans2 += 1
    elif int(r1) <= int(l1) <= int(r2) or int(r1) <= int(l2) <= int(r2) :
        ans2 += 1

print(f"{ans2=}") 
