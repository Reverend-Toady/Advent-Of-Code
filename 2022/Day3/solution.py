### PART ONE ###
with open("testcase.txt", "r") as f:
    ans1 = sum(
        [
            ord(e[0]) - 96 if e[0].islower() else ord(e[0]) - 38
            for e in [
                list(set(i[: len(i) // 2]).intersection(set(i[len(i) // 2 :])))
                for i in f.read().splitlines()
            ]
        ]
    )

print(f"{ans1}")

### PART TWO ###
with open("testcase.txt", "r") as f:
    data = f.read().splitlines()
    ans2 = sum(
        [
            ord(e[0]) - 96 if e[0].islower() else ord(e[0]) - 38
            for e in [
                list(set(sl[0]).intersection(set(sl[1]).intersection(set(sl[2]))))
                for sl in [data[j : j + 3] for j in range(0, len(data), 3)]
            ]
        ]
    )

print(f"{ans2=}")
