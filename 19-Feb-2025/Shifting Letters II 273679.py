# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        

        ans = [0] * (len(s)+1)

        for start, end, dire in shifts:
            if dire:
                ans[start]+=1
                ans[end+1]-=1
            else:
                ans[start]-=1
                ans[end+1]+=1

        for i in range(1, len(ans)):
            ans[i]+=ans[i-1]

        res = ""






        print(ans)

        for i in range(len(s)):
            val = ord(s[i]) - 97
            ans[i]+=val

        for i in range(len(ans)-1):
            ind = ans[i] % 26
            res += chr(97+ind)
        
        return res