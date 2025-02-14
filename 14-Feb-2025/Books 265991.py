# Problem: Books - https://codeforces.com/contest/279/problem/B

from collections import defaultdict, Counter, deque
import math

def IN(): return int(input())
def IS(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return list(map(str, input().split()))
def IMN(): return map(int, input().split())
def IMS(): return map(str, input().split())



def solve():
    
    a, n = IMN()
    
    arr= IL()
    
    
    res = 0 
    wind = 0
    l = 0
    
    for i in range(len(arr)):
        wind+=arr[i]
        
        while wind > n:
            wind-=arr[l]
            l+=1
            
        res = max(res, i-l+1)
            
    return res
            
            
        

               
    
    
 
    


t = 1
for _ in range(t):
    print(solve())


