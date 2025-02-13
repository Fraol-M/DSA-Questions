# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

from collections import defaultdict, Counter, deque
import math

def IN(): return int(input())
def IS(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return list(map(str, input().split()))
def IMN(): return map(int, input().split())
def IMS(): return map(int, input().split())



def solve():
    n = IN()
    arr = IL()
    
    
    negative = float("-inf")
    postive = 0
    
    stat1, stat2 = True, True
    if arr[0] > 0:
        stat1 = True
    
        
    
        
        res = []
        for i in range(len(arr)):
            
            if arr[i] > 0:
                if stat1 == False:
                    res.append(negative) 
                    stat1 = True
                    negative = float("-inf")    
                postive = max(postive, arr[i])
            else:
                if stat1:
                    res.append(postive)
                    stat1 = False
                    postive = 0
                negative = max(negative, arr[i])
       
        if stat1:
            res.append(postive)
        else:
            res.append(negative)
        
    else:
        stat2 =  True
        res = []
        for i in range(len(arr)):
            
            if arr[i] < 0:
                if stat2 == False:
                    res.append(postive)
                    stat2 = True
                    postive = 0
                negative = max(negative, arr[i])
            else:
                if stat2:
                    res.append(negative)
                    stat2 = False
                    negative = float("-inf")
                postive = max(postive, arr[i])
                
        
        if stat2:
            res.append(negative)
        else:
            res.append(postive)
        
    return sum(res)
                
                
        
        
        
    
    
    
    

    
        
    



t = IN()
for _ in range(t):
    print(solve())


