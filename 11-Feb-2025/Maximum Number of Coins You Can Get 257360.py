# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        

        piles.sort()

        me = 0

        left, right = 0, len(piles)-2

        while left < right:
            me+=piles[right]
            right-=2
            left+=1
        return me