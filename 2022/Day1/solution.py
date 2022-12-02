### PART ONE ###

with open("testcase.txt", "r") as f:
    ans1 = max(
        [
            sum(list(map(int, x)))
            for x in [i.split("\n") for i in f.read().split("\n\n")]
        ]
    )
print(f"{ans1=}")

### PART TWO ###
with open("testcase.txt", "r") as f:
    ans2 = sum(
        sorted(
            [
                sum(list(map(int, x)))
                for x in [i.split("\n") for i in f.read().split("\n\n")]
            ]
        )[::-1][:3]
    )
print(f"{ans2=}")
