# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        

        dic = defaultdict(int)
        filler =k
        l = 0
        length = 0

        for i in range(len(nums)):
            length = max(length, dic[0]+dic[1])

            if nums[i] == 1:
                dic[nums[i]]+=1 
            elif nums[i] == 0 and k > 0:
                dic[nums[i]]+=1
                k-=1

            elif nums[i] == 0 and k == 0:

                length = max(length, dic[0]+dic[1])
                while k == 0:
                    if nums[l] == 0:
                        k+=1
                    dic[nums[l]]-=1
                    if dic[nums[l]] == 0:
                        del dic[nums[l]]
                    l+=1

                dic[nums[i]]+=1
                if nums[i] == 0: k-=1
        
        length = max(length, dic[0]+dic[1])      
        return length







        
        