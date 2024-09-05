class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        b, r, w = 0, 0 ,0
        for i in range(len(nums)):
            if nums[i] == 0:
                r+=1
            elif nums[i] ==1:
                w+=1
            else:
                b+=1
        ind = 0
        for i in range(r):
            nums[ind] = 0
            ind+=1
        for j in range(w):
            nums[ind] = 1
            ind+=1
        for k in range(b):
            nums[ind] = 2
            ind+=1



        
        