class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        total = []
        a = sorted(nums)
        for i in nums:
            total.append(a.index(i))
        return total