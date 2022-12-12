import operator
from collections import defaultdict, deque
#517
#512

def readFile():
    return [list(x) for x in open("input.txt").read().strip().split('\n')]

def first_star(g):
    n = len(g)
    m = len(g[0])

    s = []
    e = []

    for i in range(n): 
        for j in range(m):
            if g[i][j] == "S":
                s = [i, j]
                g[i][j] = "a"
            if g[i][j] == "E":
                e = [i, j]
                g[i][j] = "z"

    g = [[ord(c) - 97 for c in r] for r in g]
    dst = defaultdict(lambda : 1000000)
    q = deque([(s[0],s[1])])
   
    for x,y in q:
        dst[x,y] = 0
    
    ans = 10000000
    while len(q) > 0:
        c = q.popleft()
        if c == e:
            ans = dst[e[0],e[1]]
            return ans
        for d in [(0,1),(1,0),(0,-1),(-1,0)]:
            sum = list(map(operator.add, c,d))
            if sum[0] in range(n) and sum[1] in range(m):
                if g[c[0]][c[1]] >= g[sum[0]][sum[1]] - 1:
                    ndst = dst[c[0],c[1]] + 1
                    if ndst < dst[sum[0],sum[1]]:
                        q.append(sum)
                        dst[sum[0],sum[1]] = ndst

def second_star(g):
    n = len(g)
    m = len(g[0])

    s = []
    e = []

    for i in range(n): 
        for j in range(m):
            if g[i][j] == "S":
                s = [i, j]
                g[i][j] = "a"
            if g[i][j] == "E":
                e = [i, j]
                g[i][j] = "z"

    g = [[ord(c) - 97 for c in r] for r in g]
    q = deque([(i,j) for i in range(n) for j in range(m) if g[i][j] == 0])
    dst = defaultdict(lambda : 1000000)
   
    for x,y in q:
        dst[x,y] = 0
    
    ans = 10000000
    while len(q) > 0:
        c = q.popleft()
        if c == e:
            ans = dst[e[0],e[1]]
            return ans
        for d in [(0,1),(1,0),(0,-1),(-1,0)]:
            sum = list(map(operator.add, c,d))
            if sum[0] in range(n) and sum[1] in range(m):
                if g[c[0]][c[1]] >= g[sum[0]][sum[1]] - 1:
                    ndst = dst[c[0],c[1]] + 1
                    if ndst < dst[sum[0],sum[1]]:
                        q.append(sum)
                        dst[sum[0],sum[1]] = ndst

if __name__ == "__main__":
    g = readFile()
    print(first_star(g))
    g = readFile()
    print(second_star(g))
