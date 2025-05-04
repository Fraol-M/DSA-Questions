# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, diff: List[int], prof: List[int], worker: List[int]) -> int:
        

        combine = []


        for i in range(len(diff)):
            combine.append([diff[i], prof[i]])


        combine.sort(key=lambda x:x[0])
        sorted_pro = []

        for i, j in combine:
            if not sorted_pro:
                sorted_pro.append(j)
            else:
                sorted_pro.append(max(sorted_pro[-1], j))


        result = 0
        diff.sort()
        
        print(diff)
        for w in worker:

            ind = bisect_right(diff, w)
            if ind != 0:
                result+=sorted_pro[ind-1]

            else:
                result+=0


        return result

        
