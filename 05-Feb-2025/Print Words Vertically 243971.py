# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        

        arr = s.split(" ")
        max_length = 0

        for i in range(len(arr)):
            cur = arr[i]
            max_length = max(max_length, len(cur))

        
        answer = [] 
        for i in range(max_length):
            temp = ""
            for j in range(len(arr)):
                
                if i < len(arr[j]):
                    temp+=arr[j][i]
                else:
                    temp+=" "
            answer.append(temp.rstrip())
        return answer
                
                
                


