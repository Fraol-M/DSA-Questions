class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        
        count = Counter(arr1)
        res= []
        arr1.sort()
        

        for i in range(len(arr2)):
            x = arr2[i]
            for i in range(count[x]):
                res.append(x)
        
        for i in range(len(arr1)):
            if arr1[i] not in set(arr2):
                res.append(arr1[i])
        return res