# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        bench_mark = (n // 3 ) + 1


        dic = Counter(nums)
        result = []
        for num, value in dic.items():

            if value >= bench_mark:
                result.append(num)
        return result


