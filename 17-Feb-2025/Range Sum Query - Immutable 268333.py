# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):


        self.arr = [nums[0]]


        for i in range(1, len(nums)):
            self.arr.append(self.arr[i-1]+nums[i])


        
        

    def sumRange(self, left: int, right: int) -> int:

        if left >0:
            return self.arr[right] - self.arr[left-1]

        return self.arr[right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)