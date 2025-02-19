# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        """
        1 1 2 2 3
        """

        running_sum = 0
        dic = defaultdict(int)
        result = 0
        for num in nums:
            running_sum+=num
            
            if running_sum == goal:
                result+=1
            
            rem = (running_sum - goal)
            if rem in dic:
                result+=dic[rem]
            dic[running_sum]+=1
        return result

            