# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

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
    
    arr = []
    
    for _ in range(n):
        arr.append(IL())
    
    """
    1 2 2 1   0, 0, 1, 1, 2, 2, 3,  3 -- 0, 2 --> 1, 3, 1, 1, 2, 
    2 4 2 4
    2 2 3 1
    2 4 2 4   (2, 1) --> (3, 2) --> (1, 0)
    
    """
    
    
    def inbound(x, y):
        return 0 <= x < n and 0 <= y <m
    
    
    
    
    
    dic_sum = defaultdict(int)
    dic_diff = defaultdict(int)
    for r in range(n):
        for c in range(m):
            diff = (r-c)
            t_sum = (r+c)
            
            dic_diff[diff]+=arr[r][c]
            dic_sum[t_sum]+=arr[r][c]
            
            
    res = 0
    
    for r in range(n):
        for c in range(m):
            diff = (r-c)
            t_sum = (r+c)
            
            val_1 = dic_diff[diff]
            val_2 = dic_sum[t_sum]
            total= val_1+val_2-arr[r][c]
            res = max(res, total)
    return res              
            
    
    
    
            





t = IN()
for _ in range(t):
    print(solve())


