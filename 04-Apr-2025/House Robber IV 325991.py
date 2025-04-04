# Problem: House Robber IV - https://leetcode.com/problems/house-robber-iv/

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        

        def isvalid(cap):
            index = 0
            steal = 0

            while index < len(nums):
                if nums[index]  <= cap:
                    steal += 1
                    index += 2
                else:
                    index += 1

            return steal >= k
 

            

     

        low, high = 1, max(nums)
        solution = high

        while low <= high:
            mid = low + (high-low) // 2

            if isvalid(mid):
                solution = mid
                high = mid-1
            else:
                low = mid+1

        return solution
