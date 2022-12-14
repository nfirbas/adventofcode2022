import numpy as np
#672
#26831

def readFile():
    fileContent = open("input.txt", mode='r').read().split("\n")
    rocks = []
    for data in fileContent:
        rocksCoordinates = data.split(" -> ") 
        temp = []
        for rock in rocksCoordinates:
            temp.append([int(rock.split(",")[0]), int(rock.split(",")[1])])

        rocks.append(temp)
    return rocks

def first_second_star(rocks, part2):
    cave = np.zeros((500, 1000))
    depth = 0

    for rock in rocks:
        for i in range(1, len(rock)):
            if rock[i][1] > depth:
                depth = rock[i][1]
            if rock[i-1][1] > depth:
                depth = rock[i][1]

            if rock[i][0] == rock [i-1][0]:
                s, b = rock[i][1], rock [i-1][1]
                if s > b:
                    b, s = s, b
                for x in range(s,b+1):
                    cave[x, rock[i-1][0]] = 2
                continue
            if rock[i][1] == rock [i-1][1]:
                s, b = rock[i][0], rock [i-1][0]
                if s > b:
                    b, s = s, b
                for x in range(s,b+1):
                    cave[rock[i-1][1], x] = 2
    depth +=2
    sand = 0
    if part2:
        cave[depth, :] = 2

    while True:
        x = 500
        if cave[0,x] != 0:
            return sand

        for i in range(0,500):
            if i > depth:
                return sand

            if cave[i+1,x] == 0:
                continue
            if cave[i+1,x-1] == 0:
                x -= 1
                continue
            if cave[i+1,x+1] == 0:
                x += 1
                continue
            if i > 490:
                return sand
            sand += 1
            cave[i,x] = 1
            break
    





if __name__ == "__main__":
    rocks = readFile()
    print(first_second_star(rocks,False))
    print(first_second_star(rocks,True))
