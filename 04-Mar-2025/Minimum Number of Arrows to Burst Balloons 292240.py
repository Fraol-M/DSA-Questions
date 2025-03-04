# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:


        points.sort(key = lambda x:(x[0], -x[1]))

        cnt = 0

        end = 1
        if len(points) == 1:
            return 1
        
        print(points)

        x, y = points[0][0], points[0][1]
        while end < len(points):
            x1, y1 = points[end][0], points[end][1]

            if x1 >= x and x1 <= y:
                if end == len(points)-1:
                    cnt+=1
                x = x1
                y = y if y <= y1 else y1
                end+=1
            else:
                if end == len(points)-1:
                    cnt+=1
                x = x1
                y = y1
                cnt+=1
                end+=1
            


            
        return cnt


        



        return 0