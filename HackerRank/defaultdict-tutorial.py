# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

dit = {}

n, m = map(int, input().split())


for i in range(n):
    x = input()
    if x not in dit:
        dit[x] = [i]
    else:
        dit[x].append(i)
   
    
# 

b = []

for _ in range(m):
    b.append(input())


for c in b:
    if c in dit:
        y = dit[c]
        res = []
        for i in range(len(y)):
            res.append(y[i]+1)
        print(*res)
    else:
        print(-1)


