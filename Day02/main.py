ROCK = "A"
PAPER = "B"
SCISSORS = "C"

#11767
#13886

def readFile():
    games = []

    f = open("./input.txt", "r")
    for x in f.readlines():
        temp = x.split()
        temp[1] = chr(ord(temp[1])-ord("X")+ord("A"))
        games.append(temp)
    f.close()
    return games

def rps(elf, me):
    if (me == elf):
        return 3
    if (me == ROCK and elf == SCISSORS) or (me == PAPER and elf == ROCK) or(me == SCISSORS and elf == PAPER):
        return 6
    return 0 
    
def first_star(games):
    sum = 0
    for game in games:
        sum += rps(game[0], game[1]) + ord(game[1]) - ord("A") + 1
    print(sum)

def second_star(games):
    for i in range(len(games)):
        if games[i][1] == PAPER:
            games[i][1] = games[i][0]
        else:
            games[i][1] = chr(((ord(games[i][0]) - ord("A") + 1 + int(games[i][1]==ROCK)) % 3) + ord("A"))
    first_star(games)

if __name__ == "__main__":
    games = readFile()
    first_star(games)
    second_star(games)

