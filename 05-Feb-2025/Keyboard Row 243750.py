# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        row1 = {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p"}
        row2 = {"a", "s", "d", "f","g","h","j","k","l"}
        row3 = {"z", "x", "c", "v", "b", "n", "m"}

        
        answer = []
        for word in words:
            k = set(word.lower())
            if k <= row1 or k <= row2 or k <= row3:
                answer.append(word)
           
        return answer
