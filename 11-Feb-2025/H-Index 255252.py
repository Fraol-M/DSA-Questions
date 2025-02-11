# Problem: H-Index - https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        arr = [0]*len(citations)
        citations.sort()

        """
        0, 1, 3, 5, 6
        1, 1, 3
        """
        res = 0
        n =  len(citations)
        for i in range(len(citations)):
            value = len(citations) -(i)
            print(value)
            if value <= citations[i]:
                res = max(res, value)
        

       
        return res
