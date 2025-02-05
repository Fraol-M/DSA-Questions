# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

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


