# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = Counter(nums)

        res = []
        m = 0
        for i, j in d.most_common():
            m+=1
            res.append(i)
            if m == k:
                break
        return res
