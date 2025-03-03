# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

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
    m = IN()
    arr2 = IL()
    
    
    
    maxi_1 = 0
    maxi_2 = 0
    
    x = 0
    
    
    for i in range(len(arr)):
        x+=arr[i]
        maxi_1 = max(maxi_1, x)
        
    x = 0
    for i in range(len(arr2)):
        x+=arr2[i]
        maxi_2 = max(x, maxi_2)
        
        
    print(maxi_1+maxi_2)
        

    
   
    
    
    """
    
    6 -5 7 -3 --> 6 1 8 5
    
    6 1 8 5  ----> 2 5  1
    
    2 5 1 
    
    
    
    
    
    1 1 -- . 1 2
    10 -3 2 2 -- 10 7
    
    
    6 -6 13
    6  0 13
    
    6  -1  -1
    
     
    6  5   3
    """
    
        
        
    """
    
    10
                    -5    4
    -2   -4     0   1   0  4   -4 4   3 2  -1   -1    -1  -1
    -2   -6    -6    -6    -10   -7   -8   -9   -10    -11

1 4 4 -2
    
    
-2 1 -4 4
"""
    
    
    
    
    
    
    
    
    
t = IN()
for _ in range(t):
    solve()


