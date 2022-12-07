with open("testcase.txt", "r") as f:
    data = [i.split("\n") for i in f.read().strip().split("$") if i != ""]


dirs = {}
def find_size(dir):
    return dirs[dir][1] + sum(find_size(i) for i in dirs[dir][0])

### PART ONE ###

curr_dir = ""
for command, *output in data:
    command = command.strip().split(" ")

    if command[0] == "cd":
        if command[1] == "..":
            curr_dir = "/".join(curr_dir.split("/")[:-1])
            continue

        if command[1] == "/":
            curr_dir = "/"
        else:
            if curr_dir == "/":
                curr_dir = f"/{command[1]}"
            else:
                curr_dir = curr_dir + "/" + command[1]
        dirs.update({curr_dir: 0})

    if command[0] == "ls":
        known_size = sum(
            [int(i.split(" ")[0]) for i in output if i.split(" ")[0].isnumeric()]
        )
        known_dirs = [
            curr_dir + "/" + i.split(" ")[1]
            if curr_dir != "/"
            else curr_dir + i.split(" ")[1]
            for i in output
            if i.split(" ")[0] == "dir"
        ]
        dirs.update({curr_dir: (known_dirs, known_size)})


sum_ = 0
for dir in dirs:
    if dir == "..":
        continue

    dir_size = find_size(dir)
    if dir_size <= 100000:
        sum_ += dir_size

print(sum_)

### PART TWO ###

dirs = {}
curr_dir = ""
for command, *output in data:
    command = command.strip().split(" ")

    if command[0] == "cd":
        if command[1] == "..":
            curr_dir = "/".join(curr_dir.split("/")[:-1])
            continue

        if command[1] == "/":
            curr_dir = "/"
        else:
            if curr_dir == "/":
                curr_dir = f"/{command[1]}"
            else:
                curr_dir = curr_dir + "/" + command[1]
        dirs.update({curr_dir: 0})

    if command[0] == "ls":
        known_size = sum(
            [int(i.split(" ")[0]) for i in output if i.split(" ")[0].isnumeric()]
        )
        known_dirs = [
            curr_dir + "/" + i.split(" ")[1]
            if curr_dir != "/"
            else curr_dir + i.split(" ")[1]
            for i in output
            if i.split(" ")[0] == "dir"
        ]
        dirs.update({curr_dir: (known_dirs, known_size)})

needed = 30000000 - (70000000 - find_size("/"))

dir_size = []
for dir in dirs:
    if dir == "..":
        continue
    
    if dir == "/":
        continue

    dir_size_ = find_size(dir)
    if dir_size_ >= needed:
        dir_size.append((dir, dir_size_))

print(sorted(dir_size, key= lambda i: i[1])[0][1])