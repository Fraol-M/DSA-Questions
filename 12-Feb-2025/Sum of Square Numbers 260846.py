# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """

         1 2 3 4 5

         3 4 5 1 2

         3 4 5 1 2
        """

        left = 0
        right = int(math.sqrt(c))
        print(right)

        while left <= right:
            value = (left**2) + (right**2)
            if value == c:
                return True
            elif value > c:
                right-=1
            else:
                left+=1
    
        return False


