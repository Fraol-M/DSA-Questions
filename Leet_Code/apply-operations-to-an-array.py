from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        start, end = 0, 1
    
        while end < len(nums):
            if nums[start] == nums[end]:
                nums[start] = 2 * nums[start]
                nums[end] = 0
            start = end
            end+=1
        k = []
        cnt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                k.append(nums[i])
            else:
                cnt+=1
        for i in range(cnt):
            k.append(0)
        return k

        