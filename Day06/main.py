def readFile():
    return open("input.txt", mode='r').read()

def first_second_star(dataStream, matchingChar):
    for i in range(len(dataStream)):
        if len(set(dataStream[i:i+matchingChar])) == matchingChar:
            return i + matchingChar 

if __name__ == "__main__":
    data = readFile()
    print(first_second_star(data,4))
    print(first_second_star(data,14))
  


