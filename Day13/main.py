from functools import cmp_to_key

#5557
#22425

def readFile():
    fileContent = open("input.txt", mode='r').read().split("\n\n")
    packets = []
    for data in fileContent:
        data = data.split("\n") 
        packets.append(eval(data[0]))
        packets.append(eval(data[1]))
    return packets


def compare(left, right):
    match left, right:
        case int(), int():  return (left>right) - (left<right)
        case int(), list(): return compare([left], right)
        case list(), int(): return compare(left, [right])
        case list(), list():
            for z in map(compare, left, right):
                if z: return z
            return compare(len(left), len(right))

def first_star(packets):
    sum = 0
    for i in range(0,len(packets), 2):
        if compare(packets[i], packets[i+1]) == -1:
            sum += i/2 + 1 
    print(int(sum))


def second_star(packets):
    decoderKey = 1
    packets.append([[2]])
    packets.append([[6]])
    packets = sorted(packets, key=cmp_to_key(compare))
    for i in range(len(packets)):
        if packets[i] == [[6]] or packets[i] == [[2]]:
            decoderKey *= (i+1)
    
    print(int(decoderKey))



if __name__ == "__main__":
    packets = readFile()
    first_star(packets)
    second_star(packets)
