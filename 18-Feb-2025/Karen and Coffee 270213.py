# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

from collections import defaultdict, Counter, deque
import math

def IN(): return int(input())
def IS(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return list(map(str, input().split()))
def IMN(): return map(int, input().split())
def IMS(): return map(int, input().split())



def solve():
    n, k, m = IMN()
    
    temp=[]
    mini = float("inf")
    maxi = float("-inf")
    
    for _ in range(n):
        arr = IL()
        
        mini = min(arr[0], mini)
        maxi = max(arr[1], maxi)
        temp.append(arr)
        
    question = []
   
    
    for _ in range(m):
        question.append(IL())

    
    ans = [0] * 200002
    
    
    
    
    for l, r in temp:
        
        
        ans[l] += 1
        ans[r+1] += -1
        
      
      
    for i in range(1, len(ans)):
        ans[i] += ans[i-1]  
        
      
     
                        
   
    
    for i in range(len(ans)):
        if ans[i] < k:
            ans[i] = 0
        else:
            ans[i] = 1
            
    
    for i in range(1, len(ans)):
        ans[i]+=ans[i-1]
        
    

    result = []
    
    for x, y in question:
        
        val = ans[y] - ans[x-1]    
        result.append(val)
        
    for j in result:
        print(j)
    
    
    
    
    
        
        
        
    


        
    
    

t = 1
for _ in range(t):
    solve()


