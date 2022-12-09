#6243
#2630

def readFile():
    moves = []
    f = open("./input.txt", "r")
    for x in f.readlines():
        temp = x.split()
        temp[1] = int(temp[1])
        moves.append(temp)
    f.close()
    return moves

def direction(x):
    if x < 0:
        return -1
    if x > 0:
        return 1 
    return 0

def first_second_start(moves, length):
    knots = [[0, 0] for _ in range(length)]
    visited = {tuple(knots[-1])}

    for move in moves:
        for _ in range(move[1]):
            match move[0]:
                case 'L':
                    knots[0][0] += -1
                case 'R':
                    knots[0][0] += 1
                case 'U':
                    knots[0][1] += -1
                case 'D':
                    knots[0][1] += 1
            
            for i in range(1, len(knots)):
                x = knots[i-1][0] - knots[i][0]
                y = knots[i-1][1] - knots[i][1]

                if abs(x) > 1 or abs(y) > 1:
                    knots[i][0] += direction(x)
                    knots[i][1] += direction(y)
            visited.add(tuple(knots[-1]))
    print(len(visited))


if __name__ == "__main__":
    moves = readFile()
    first_second_start(moves, 2)
    first_second_start(moves, 10)
