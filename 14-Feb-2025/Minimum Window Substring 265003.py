# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:


        dic= Counter()
        count = Counter(t) 

        l = 0

        res1, res2 = 0, 0
        size = float("inf")
        
        for i in range(len(s)):
            
            dic[s[i]]+=1

            while dic >= count:
         
                

                if (i-l+1) < size:
                    size = i-l+1
                    res1 = l
                    res2 = i

                
                dic[s[l]]-=1
                if dic[s[l]] == 0:
                    del dic[s[l]]
                l+=1


        
        if size == float("inf"):
            return ""

        return s[res1:res2+1]
        