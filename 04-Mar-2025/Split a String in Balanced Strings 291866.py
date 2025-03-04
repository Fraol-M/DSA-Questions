# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        r_count = 0
        l_count = 0
        res = 0

        for c in s:
            if c == "R":
                r_count+=1
            else:
                l_count+=1
            if r_count == l_count:
                res+=1
                r_count, l_count = 0, 0

        return res
        

        