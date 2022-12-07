from collections import defaultdict

#1118405
#12545514

def readFile():
    return open("input.txt", mode='r').read().splitlines()

def first_star(commands):
    dirPath = []
    dirSizes = defaultdict(int)
    for command in commands:
        match command.split(" "):
            case ["$", "cd", ".."]:
                dirPath.pop()
            case ["$", "cd", dir]:
                dirPath.append("/".join(dirPath) + dir)
            case ["$", "ls"]:
                continue
            case [sizeStr, _] if sizeStr != "dir":
                for v in dirPath:
                    dirSizes[v] += int(sizeStr)

    total = 0
    for size in dirSizes.values():
        if size <= 100_000:
            total += size
    print(total)

def second_star(commands):
    dirPath = []
    dirSizes = defaultdict(int)
    for command in commands:
        match command.split(" "):
            case ["$", "cd", ".."]:
                dirPath.pop()
            case ["$", "cd", dir]:
                dirPath.append("/".join(dirPath) + dir)
            case ["$", "ls"]:
                continue
            case [sizeStr] if sizeStr != "dir":
                for v in dirPath:
                    dirSizes[v] += int(sizeStr)

    remaining = dirSizes["/"] - 40_000_000
    best = 100_000_000
    for size in dirSizes.values():
        if size >= remaining and best > size:
            best = size
    print(best)

if __name__ == "__main__":
    commands = readFile()
    first_star(commands)
    second_star(commands)