class Solution:
    def freqAlphabets(self, s: str) -> str:
        alp = {}
        for i in range(97, 123):
            alp[(i-97)+1] = chr(i)
    
        re = ""
        start, end = 0, 0
        while start < len(s):
            k = ""
            if end+2 < len(s) and (s[end] == "1" or s[end] == "2") and (s[end+2] == "#"):
                k = s[end] + s[end+1]  
                start += 3

                re = re + alp[int(k)]
            else:
                if s[end] != "#":
                    start+=1

                    re = re + alp[int(s[end])]
            end = start
        return re




                

        

        
        
        