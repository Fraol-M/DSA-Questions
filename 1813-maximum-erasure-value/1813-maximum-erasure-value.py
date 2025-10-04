class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        left = 0
        total_sum = 0
        ans = 0
        unique = set()

        for right in range(len(nums)):
            
            while nums[right] in unique:
                total_sum -= nums[left]
                unique.remove(nums[left])
                left+=1

            total_sum+= nums[right]
            unique.add(nums[right])
            ans = max(ans, total_sum)

        return ans 