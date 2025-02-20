# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
        
        """


        [y x y 0 0 xy 0 0 x 0 y 0 0 y 0 x    x            y      y]

        [1]


        """

        if first and second:
            maximum = max(first[-1][-1], second[-1][-1])
        
        else:
            return []
        

        i, j = 0, 0
        res = []
        while i < len(first) and j < len(second):
            cur_1 = first[i]
            cur_2 = second[j]
            print(cur_1, cur_2)
            if cur_1[0] <= cur_2[-1] and cur_2[0] <= cur_1[-1]:
                print("1")
                x = max(cur_1[0], cur_2[0])
                y = min(cur_1[-1], cur_2[-1])

                res.append([x, y])

                if cur_1[-1] > cur_2[-1]:
                    j+=1
                elif cur_1[-1] < cur_2[-1]:
                    i+=1
                else:
                    i+=1
                    j+=1
            else:
                if cur_1[-1] > cur_2[-1]:
                    j+=1
                elif cur_1[-1] < cur_2[-1]:
                    i+=1
                else:
                    i+=1
                    j+=1
               
        return res


        