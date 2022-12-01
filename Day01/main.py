def readFile():
    elves = []
    elves.append([])

    f = open("./input.txt", "r")
    for x in f.readlines():
        if x == "\n":
            elves.append([])
        else :
            elves[len(elves)-1].append(int(x))
    f.close()
    elves.sort(key=sum, reverse=True)
    return elves

def first_star():
        print(sum(elves[0]))
    
def second_star():
    print(sum(elves[0])+sum(elves[1])+sum(elves[2]))

if __name__ == "__main__":
    elves = readFile()

    first_star()
    second_star()


