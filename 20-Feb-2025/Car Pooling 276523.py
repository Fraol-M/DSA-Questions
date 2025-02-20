# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = len(trips)
        arr = []
        for pas, from_, to in trips:
            arr.append([to, -pas])
            arr.append([from_, pas])
            

        arr.sort(key=lambda x:(x[0], x[1]))
        cur = 0
        print(arr)

        
        for i in range(len(arr)):
            cur+=arr[i][1]
            if cur > capacity:
                return False
        return True


        
        