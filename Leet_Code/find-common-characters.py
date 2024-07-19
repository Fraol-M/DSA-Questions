class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
    
        new = set(words[0])
        res = ""
            
        for s in new:
           
            freq = min([word.count(s) for word in words])
            print([word.count(s) for word in words])
 

            res += s*freq
        
        return res


