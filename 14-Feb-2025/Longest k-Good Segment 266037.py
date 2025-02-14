# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict, Counter, deque
import math

def IN(): return int(input())
def IS(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return list(map(str, input().split()))
def IMN(): return map(int, input().split())
def IMS(): return map(int, input().split())



def solve():
    n, m = IMN()
    arr = IL()
    
    dic = defaultdict(int)
    
    left = 0
    diff = 0
    
    x, y = 0, 0
    
    
    for i in range(len(arr)):
        
        
        dic[arr[i]]+=1
        
        while len(dic) > m:
            dic[arr[left]]-=1
            if dic[arr[left]] == 0:
                del dic[arr[left]]
            left+=1
        
        
  
          
        if (i-left+1) > diff:
            diff = (i-left+1)
            x = i+1
            y = left+1
    return y, x
                
            
                
        
        
        
    
    
            
    
    
    
    
 
    


t = 1
for _ in range(t):
    print(*solve())


