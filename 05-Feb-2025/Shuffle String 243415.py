# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        res = [""]*len(s)
        i = 0
        for num in indices:
            res[num] = s[i]
            i+=1
        return "".join(res)
        