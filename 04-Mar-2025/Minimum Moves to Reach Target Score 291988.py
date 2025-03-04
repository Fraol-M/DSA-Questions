# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, tg: int, maxD: int) -> int:
        

        rem_cnt = 0
        double_cnt = 0
        while maxD and tg > 1:

            if tg % 2:
                rem_cnt+=1
            tg = tg // 2
            double_cnt+=1
            maxD-=1

        
            
        ans = rem_cnt + tg-1 + double_cnt


        """

        rem = 1
        10 -- 5 --2 -- 1

        19
        
        cnt = 2
        18 -- 8 -- 4

        2   10

        4-1

        """
        return ans
       
