class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        k = 0
        start , end = 0, 1
        status = True

       
        while end < len(arr):
            if arr[start] < arr[end]:
                start+=1
                end+=1
            elif arr[start] == arr[end]:
                status = False
                break
            else:
                k = start
                break
        if status == False or k == 0:
            return False
        else:
            for i in range(k, len(arr)-1):
                if arr[i] < arr[i+1] or arr[i] == arr[i+1]:
                    status = False
                    break
            return status 

                        
        



