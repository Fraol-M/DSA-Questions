# Problem: D - Final Strength - https://codeforces.com/gym/601269/problem/D

 
import sys, threading
 
input = lambda: sys.stdin.readline().strip()
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def IN(): return int(input())
def IL(): return list(map(int, input().split()))
def IMN(): return map(int, input().split())
 
def main():
          
    def solve():
        n = IN()
        arr = IL()
        
        arr_2 = []
        for i in range(len(arr)):
            arr_2.append([arr[i], i])
        
        
       
        
        def merge(left, right):
            arr = []
            
            val_left = []
            val_right = []
            for c in left:
                val_left.append(c[0])
            for c in right:
                val_right.append(c[0])
            
            for i in range(len(val_left)):
                val = left[i][0]
                ind = bisect_left(val_right, val)
                
                left[i][0]+=ind
                
            for i in range(len(val_right)):
                val = right[i][0]
                ind = bisect_left(val_left, val)
                right[i][0]+=ind
           
            # print(left, right)
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i][0] <= right[j][0]:
                    arr.append(left[i])
                    i += 1
                else:
                    arr.append(right[j])
                    j += 1
                
 
            arr.extend(left[i:])
            arr.extend(right[j:])
            
            # print(arr)
            # print()
            
         
            return arr
                            
                
                    
            
            
        
        
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
 
            mid = len(arr) // 2
            left_half = merge_sort(arr[:mid])
            right_half = merge_sort(arr[mid:])
            
            # print(left_half, right_half)
 
            return merge(left_half, right_half)
 
        
        
        
        
 
        res = [0]*len(arr) 
        for val, ind in merge_sort(arr_2):
            res[ind] = val
            
        print(*res)
        
 
    t = IN()
    for _ in range(t):
        solve()
 
 
 
 
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)
 
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()