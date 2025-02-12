# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

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
    arr = set(IL())
    
    # 1 2 3 4 5
    
    
    cur_pos = 1
    if cur_pos in arr: return "NO"
    while cur_pos < n:
        
        if cur_pos+3 not in arr and cur_pos+3 <= n:
            cur_pos+=3
        elif cur_pos+2 not in arr and cur_pos+2 <= n:
            cur_pos+=2
        elif cur_pos+1 not in arr and cur_pos+1 <= n:
            cur_pos+=1
        else:
            return "NO"
    return "YES"
    
    
    
    
        
    
    
            
    

t = 1
for _ in range(t):
    print(solve())


