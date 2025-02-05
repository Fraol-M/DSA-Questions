# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

from collections import defaultdict, Counter, deque
import math

def IN(): return int(input())
def IS(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return list(map(str, input().split()))
def IMN(): return map(int, input().split())
def IMS(): return map(int, input().split())



def solve():
    
    s = IS()
    t = IS()
    p = IS()
    
    k3 = Counter(p)

    i, j = 0, 0
    
    if len(s) > len(t):
        return "NO"
    
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j+=1
        elif s[i] != t[j]:
            if t[j] in k3:
                k3[t[j]]-=1
                if k3[t[j]] == 0:
                    del k3[t[j]]
            else:
                return "NO"  
            j += 1
        
        
    while j != len(t):
        cur = t[j]
        if cur in k3:
            k3[cur]-=1
            if k3[cur] == 0:
                del k3[cur]
            j+=1
        else:
            return "NO"
        
        
        
    return "YES"
    
    # k1 = Counter(s)
    # k2 = Counter(t)
    
    
    # for char, count_t in k2.items():
    #     count_s = k1.get(char, 0) 
    # 
    
        
    
    


for _ in range(IN()):
    
    print(solve())
    
                    
    