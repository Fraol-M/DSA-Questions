# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        

        """


        1 -3 2 3 -4
        1 2 4 7 5

        2 -5 1 -4 3 -2

        2 -3 -2 -6 -5 -7
        """

        psum = []

        x= 0

        for num in nums:
            x+=num
            psum.append(x)

        print(psum)

        postive = 0
        negative = 0

        ans = float("-inf")
        for i in range(len(psum)):
            cur = psum[i]

            if cur < 0:
                negative = min(cur, negative)
                res = abs(cur - postive)
                print(res, "res", i, cur, postive)
            elif cur >= 0:
                postive = max(cur, postive)
                res = abs(cur - negative)

            ans = max(ans, abs(res))

        return ans

            
            