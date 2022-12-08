from collections import defaultdict

#1843
#180000

def readFile():
    forest = []
    with open('input.txt') as f:
            for line in f.readlines():
                forest.append(list(map(int, line.strip())))
    return forest

def first_star(forest):
    visible = 0
    width = len(forest)
    length = len(forest[0])

    for i in range(width):
        for j in range(length):
            if i == 0 or j == 0 or i == length-1 or j == width - 1:
                visible += 1 
                continue
            
            if max(forest[i][:j]) < forest[i][j]:
                visible += 1 
                continue
           
            if max(forest[i][j+1:]) < forest[i][j]:
                visible += 1 
                continue
            
            if max([forest[x][j] for x in range(i)]) < forest[i][j]:
                visible += 1 
                continue

            if max([forest[x][j] for x in range(i+1, length)]) < forest[i][j]:
                visible += 1 
                continue

    print(visible)


def second_star(forest):

    maxScore = 1
    width = len(forest)
    length = len(forest[0])

    for i in range(width):
        for j in range(length):
            if i == 0 or j == 0 or i == length-1 or j == width - 1:
                continue

            score = 1
            visible = 0 
            for x in range(j-1, -1, -1):
                visible += 1
                if forest[i][x] >= forest[i][j]: 
                    break
            score *= visible
            visible = 0

            for x in range(j+1, width):
                visible += 1
                if forest[i][x] >= forest[i][j]: 
                    break
            score *= visible
            
            visible = 0

            for x in range(i-1, -1, -1):
                visible += 1
                if forest[x][j] >= forest[i][j]: 
                    break
            score *= visible
            visible = 0

            for x in range(i+1, length):
                visible += 1
                if forest[x][j] >= forest[i][j]: 
                    break
            score *= visible
            
            maxScore = max([maxScore, score])


    print(maxScore)


   

if __name__ == "__main__":
    forest = readFile()
    first_star(forest)
    second_star(forest)