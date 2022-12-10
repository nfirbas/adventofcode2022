#15680
#ZFBFHGUP

def readFile():
    instructions = []
    f = open("./input.txt", "r")
    for x in f.readlines():
        temp = x.split()
        instructions.append(temp)
    f.close()
    return instructions + ([["nop"]]* (240-len(instructions)))



def first_start(instructions):
    register = 1
    sum = 0
    waitList = []
    crt = []
    for i in range(len(instructions)):
        waitList.append(0)
        if instructions[i][0] == "addx":
            waitList.append(int(instructions[i][1]))

        if (i+1) in [20,60,100,140,180,220]:
            sum += (i+1) * register

        if register in [i%40, (i+1)%40, (i-1)%40]:
            crt.append("#")
        else:
            crt.append(".")
        
        #after
        register += waitList[0]
        waitList[:] = waitList[1:]

    print(sum)
    print(crt[0:40])
    print(crt[40:80])
    print(crt[80:120])
    print(crt[120:160])
    print(crt[160:200])
    print(crt[200:240])

if __name__ == "__main__":
    instructions = readFile()
    first_start(instructions)
