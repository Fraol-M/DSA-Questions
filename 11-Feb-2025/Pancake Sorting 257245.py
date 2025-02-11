# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        


        """
        [2, 2. 2]

        3 2 4 1 --> 2 3 4 1 --2 3 1 4 -- 2 1 3 4


        3 2 4 1

        """

        """

        4, 3, 2, 1


        for i in arr:
            
        """
        res = []
        maximum_number = len(arr)
        for i in range(len(arr)):
            ind = arr.index(maximum_number)
            arr[:ind+1] = arr[:ind+1][::-1]
            res.append(ind+1)
            arr[:maximum_number] = arr[:maximum_number][::-1]
            res.append(maximum_number)
            maximum_number-=1

        return res


            


