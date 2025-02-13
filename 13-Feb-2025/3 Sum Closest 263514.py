# Problem: 3 Sum Closest - https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:


        cnt = 0
        d = float("inf")
        nums.sort()
        # 0 1 1  1
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1

            while left < right:
                value = nums[i]+nums[left]+nums[right]
                distance = abs(target - value)
                if d > distance:
                    d = distance
                    cnt = value
                    print(value)
                
                if value < target:
                    left+=1
                else:
                    right-=1
        return cnt

        
