#7817
#2444
def readFile():
    return open("input.txt", mode='r').read().splitlines()

def second_star(rucksacks):
    sum = 0
    for i in range(0, len(rucksacks), 3):
        badge = list(set(rucksacks[i]) & set(rucksacks[i+1]) & set(rucksacks[i+2]))[0]
        sum += calculateBadge(badge)
    print(sum)

def first_star(rucksacks):
    sum = 0
    for rucksack in rucksacks:
        firstCompartment, secondCompartment = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        badge = ''.join(set(firstCompartment).intersection(secondCompartment))[0]
        sum += calculateBadge(badge)
    print(sum)
 
def calculateBadge(badge): 
    value = 0
    if ord(badge) < 97:
        value += ord(badge) - ord("A") + 27
    else: 
        value += ord(badge) - ord("a") + 1
    return value
if __name__ == "__main__":
    rucksacks = readFile()
    first_star(rucksacks)
    second_star(rucksacks)

