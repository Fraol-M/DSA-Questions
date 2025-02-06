# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        


        result = 0
        seen = defaultdict(int)
     

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product = nums[i] * nums[j]
                seen[product]+=1

        for j in seen.values():
            if j > 2:
                k = j*(j-1)/2
                result+= (k*8)
            elif j == 2:
                result+=8
        
        return int(result)
