# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        start = 1
        res = [0]* len(nums)
        ans = []
        for i in range(len(nums)):

            if res[nums[i]-1] == 0: 
                res[nums[i]-1] = nums[i]
            else:
                ans.append(nums[i])

        print(res)

        for i in range(len(res)):
            if res[i] == 0:
                ans.append(i+1)

        return ans

