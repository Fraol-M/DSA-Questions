class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:


        ranges.sort()
    

        for i in range(len(ranges)):
            cur = ranges[i]

            
            
            while left >= cur[0] and left <= cur[1]:
                
                if left == right:
                    return True
                left+=1
        return False








