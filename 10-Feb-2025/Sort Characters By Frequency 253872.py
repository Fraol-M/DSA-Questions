# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        
        count = Counter(s)

        res = ""
        for i, j in count.most_common():
            res += j*i
        return res
