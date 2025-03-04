# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        
        
        res = [""] * len(s)

        last = len(s)-2
        first = 0
        cnt = 0

        for c in s:
            if cnt == 0 and c == "1":
                res[-1] = c
                cnt+=1
            
            elif c == "0":
                res[last] = c
                last-=1
            else:
                res[first] = c
                first+=1

        return "".join(res)
