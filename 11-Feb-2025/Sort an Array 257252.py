# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        
        arr = [0]*(max(nums)+1)
        minimum_number = min(nums)
        stat = False
        if minimum_number < 0:
            stat = True
            below_zero = [0]*(abs(minimum_number)+1)



            
        for i in range(len(nums)):
            num = nums[i]
            if num < 0:
                below_zero[abs(num)]+=1
            else:            
                arr[num]+=1

        res = []
        if stat:
            for i in range(len(below_zero)-1, -1, -1):
                cur = below_zero[i]
                for j in range(cur):
                    res.append(-i)
            print(res)
        
        for i in range(len(arr)):
            for j in range(arr[i]):
                res.append(i)
        

        return res
