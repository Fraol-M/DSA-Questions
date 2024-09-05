class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1.sort()
        nums2.sort()

        start, end = 0, 0
        res = []

        while start < len(nums1) and end < len(nums2):
            if nums1[start] == nums2[end]:
                res.append(nums1[start])
                start+=1
                end+=1
            elif nums1[start] > nums2[end]:
                end+=1
            else:
                start+=1
        return res

        