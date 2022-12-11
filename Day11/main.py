class Monkey:
    def __init__(self, items, operation,divisibleBy, true, false ):   
        self.items = items
        self.operation = operation
        self.divisibleBy = divisibleBy
        self.true = true
        self.false = false
        self.inspected = 0
    def getInspected(self):
        return  self.inspected



 
def readFile():
    fileContent = open("input.txt", mode='r').read().split("\n\n")
    monkeys = []
    for data in fileContent:
        data = data.split("\n") 
        monkeys.append(Monkey(list(map(int, data[1].removeprefix("  Starting items: ").split(","))),
            data[2].removeprefix("  Operation: new = "),
            int(data[3].removeprefix("  Test: divisible by ")),
            int(data[4].removeprefix("    If true: throw to monkey ")),
            int(data[5].removeprefix("    If false: throw to monkey "))))

    return monkeys


def second_star(monkeys, runs, useDivide):
    denominator = 1
    for monkey in monkeys:
        denominator *= monkey.divisibleBy

    for _ in range(runs):
        for i in range(len(monkeys)):
            for _ in range(len(monkeys[i].items)):
                monkeys[i].items[0] = int(eval(monkeys[i].operation.replace("old", str(monkeys[i].items[0]))))
                
                if useDivide:
                    monkeys[i].items[0] = int(monkeys[i].items[0] / 3)
                if monkeys[i].items[0] > denominator:
                    monkeys[i].items[0] = int(monkeys[i].items[0] % denominator)

                if monkeys[i].items[0]%monkeys[i].divisibleBy==0:
                    monkeys[monkeys[i].true].items.append(monkeys[i].items[0])
                else:
                    monkeys[monkeys[i].false].items.append(monkeys[i].items[0])

                monkeys[i].inspected +=1
                monkeys[i].items = monkeys[i].items[1:]

    temp = []
    for i in monkeys:
        temp.append(i.inspected)
    monkeys.sort(key=Monkey.getInspected, reverse=True)
    print(monkeys[0].inspected*monkeys[1].inspected)


if __name__ == "__main__":
    monkeys = readFile()
    second_star(monkeys, 20, True)
    monkeys = readFile()
    second_star(monkeys, 10000, False)


