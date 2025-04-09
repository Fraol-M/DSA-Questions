# Problem: C - Ras Alula and The Decrypted Messages - https://codeforces.com/gym/601269/problem/C

from collections import defaultdict, Counter, deque
import math
def IN(): return int(input())
def IS(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return list(map(str, input().split()))
def IMN(): return map(int, input().split())
def IMS(): return map(str, input().split())
 
 
 
 
def solve():
    
    n, m = IMN()
    s = IS()
    m = IS()
    
    word_count = 0
    
    for c in m:
        word_count+=ord(c)
        
    
    left = 0
    cnt = 0
    for i in range(len(s)):
        cnt+=ord(s[i])
        
        
        if i-left+1 == len(m):
            if cnt == word_count:
                print("YES")
                return
            cnt-=ord(s[left])
            left+=1
            
            
    print("NO")
    
            
 
t = IN()
for _ in range(t):
    solve()