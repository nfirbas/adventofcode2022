#7817
#2444
def readFile():
    return open("input.txt", mode='r').read().splitlines()

def first_star(rucksacks):
    count = 0
    for pair in pairs:
        assignments = list(map(int, pair.replace("-", ",").split(",")))
        if assignments[0] <= assignments[2] and assignments[3] <= assignments[1] or assignments[2] <= assignments[0] and assignments[1] <= assignments[3]:
            count +=1
    print(count)

def first_second(rucksacks):
    count = 0
    for pair in pairs:
        assignments = list(map(int, pair.replace("-", ",").split(",")))
        if (assignments[2] <= assignments[1] and assignments[0] <= assignments[3]):
            count +=1
    print(count)


if __name__ == "__main__":
    pairs = readFile()
    first_star(pairs)
    first_second(pairs)

