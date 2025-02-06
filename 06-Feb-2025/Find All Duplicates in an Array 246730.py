# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        count = Counter(nums)


        res = []
        for i, j in count.items():
            if j >= 2:
                res.append(i)
        return res
