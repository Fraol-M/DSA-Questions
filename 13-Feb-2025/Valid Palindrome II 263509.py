# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:


        left, right = 0, len(s)-1
        forward, backward = 0, 0
        cnt = 1
        stat = True
       
        while left < right:
            if cnt and s[left] != s[right]:
                cnt-=1
                backward = right
                forward = left
                left+=1
            elif cnt == 0 and s[left] != s[right]:
                stat = False
                break
            else:
                left+=1
                right-=1

        if stat:
            return True

        backward-=1
        while forward < backward:  
            if s[forward] != s[backward]:
                return False
            else:
                forward+=1
                backward-=1
        

        return True


        