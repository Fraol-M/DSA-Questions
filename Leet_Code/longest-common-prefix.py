class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        k = []
        for i in range(len(strs[0])):
            k.append(strs[0][i])
        start, end = 0, 1
      
        if len(strs) == 1:
            return strs[0]
        h = ""
        r = ""       
       
        while end < len(strs):
            for i in range(len(strs[end])):
                if r == "":
                    if i < len(k) and k[i] == strs[end][i]:
                        h = h + k[i]
                    else:
                        break
                elif r != "":     
                    if i < len(r) and r[i] == strs[end][i]:
                        h = h + r[i]
                else:
                    break
            if end == 1 and h == "":
                r= h
                break
            r = h
            h = ""
            end+=1
        return r


            
