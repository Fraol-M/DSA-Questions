# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

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
    
    
    ans_1 = [0]
    x = 0
    
    sorted_arr = []
    ans_2 = [0]
    
    for i in range(len(arr)):
        x+=arr[i]
        ans_1.append(x)
    
    for _ in range(m):
        ty, l, r = IMN()
        
        if ty == 1:  
            print(ans_1[r]-ans_1[l-1])
        else:
            if not sorted_arr:
                sorted_arr = sorted(arr)
              
                
                x = 0
                
                for i in range(len(sorted_arr)):
                    x+=sorted_arr[i]
                    ans_2.append(x)
                    
            print(ans_2[r]-ans_2[l-1])
            
            
        

    
    
    
    
    return
    
    # for _ in range(m):
    #     ty, l, r = IMN()
    #     if ty == 1:
    #         print(ans[r-1]-ans[l-1])
    #     else:
            
    #         if not sorted_arr:
                
    #             sorted_arr = sorted(arr)
    #             ans2 = [0]
    #             x = 0
                
    #             for num in sorted_arr:
    #                 x+=num
    #                 ans2.append(x)
                    
    #         print(ans2[r-1]- ans2[l-1])
                
            
     
    
    
    
    
    """
    
    6 4 2 7 2 7
    
    
    """
        
    
    
    
    
        
        
        
    


        
    
    

t = 1
for _ in range(t):
    solve()


