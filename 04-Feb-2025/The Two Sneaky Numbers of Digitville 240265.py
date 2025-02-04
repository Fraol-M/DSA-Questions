# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        

        dic = Counter(nums)


        result = []

        for i , j in dic.items():
            if j >1 :
                result.append(i)
        return result
