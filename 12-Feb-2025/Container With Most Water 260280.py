# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:


        left, right = 0, len(height)-1

        result = 0
        while left < len(height):
            width = right - left 
            
            if height[left] <= height[right]:
                area = width * height[left]
                print(area, "area", left, right, width)

                result = max(result, area)
                left+=1
            elif height[left] > height[right]:

                area = width * height[right]
                print(area, "area", left, right, width, "second")

                result = max(result, area)
                right-=1
        return result 
            



        