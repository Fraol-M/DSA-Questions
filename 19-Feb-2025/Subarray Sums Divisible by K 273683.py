# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        # 4,5,0,-2,-3,1
        # 1+1+1 
        # 4 9 9 7 4 5
        #          
        
        """
        
        1+1+1+1+1
        1- 5
        1 - 5, 0
        1 -5 0 -2 -3
        1 - 0 -2 -2
        
        1 -5
        4 5 0 -2 -3 1
        4 9 9  7  4  5
         

        """


        dic = defaultdict(int)
        cur_sum = 0

        result = 0
        for num in nums:
            cur_sum+=num
            if cur_sum % k == 0:
                result+=1

            module = cur_sum % k
            if module in dic:
                result+=dic[module]
            dic[module]+=1
        return result
