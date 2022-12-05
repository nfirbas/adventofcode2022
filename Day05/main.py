import re


def readFile():
    return open("input.txt", mode='r').read().split("\n\n")


def getData():
    data = readFile()
    first = True
    stacks = []
    for line in data[0].split("\n")[:-1]:
        for pos, index in enumerate(range(1, len(line), 4)):
            if first:
                stacks.append([])
            if line[index] != " ":
                stacks[pos] = [line[index]] + stacks[pos]
        first = False 

    moves = []
    for line in data[1].split("\n"):
        move = line.split(" ")
        moves.append([int(move[1]), int(move[3])-1, int(move[5])-1])
    return [stacks, moves]

def first_star(stacks, moves):
    for move in moves:
        for _ in range(move[0]):
            stacks[move[2]].append(stacks[move[1]].pop())

    for stack in stacks:
        print(stack[-1], end="")
    print('\n', end="")

def second_star(stacks, moves):
    for move in moves:
        temp = []
        for _ in range(move[0]):
            temp.append(stacks[move[1]].pop())
        temp.reverse()
        stacks[move[2]] += temp
    for stack in stacks:
        print(stack[-1], end="")
    print('\n', end="")




if __name__ == "__main__":
    data = getData()
    first_star(data[0], data[1])
    data = getData()
    second_star(data[0], data[1])


