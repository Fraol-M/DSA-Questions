class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        k = arr[-1]
        res = [-1] * len(arr)
        for i in range(len(arr)-2, -1, -1):
            res[i] = max(arr[i+1], k)
            k = max(k, res[i])
           

        return res

         
        