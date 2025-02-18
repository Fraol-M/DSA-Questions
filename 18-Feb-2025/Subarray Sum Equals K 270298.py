# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        

        dic = defaultdict(int)

        x = 0
        res = 0
        for num in nums:
            x+=num
            
            rem = x - k
            if rem in dic:
                res+=dic[rem]
            if x == k:
                res+=1

            dic[x]+=1
        return res