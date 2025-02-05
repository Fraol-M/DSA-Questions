# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], cur: List[List[int]]) -> List[int]:


        even= 0

        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even+=nums[i]
                
    




        res = []
        for val, ind in cur:

            if nums[ind] % 2 == 0:
                if val % 2 == 0:
                    even+=val
                else:
                    even-=(nums[ind])
            else:
                if val % 2 != 0:
                    even+=(nums[ind]+val)
            nums[ind] +=val
            res.append(even)
        return res


            



    
            


        