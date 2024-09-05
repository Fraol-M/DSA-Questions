class Solution:
    def sortSentence(self, s: str) -> str:
        li = list(s.split(" "))
        
        res = [0]*len(li)
        print(res)

        for i in range(len(li)):
            x = li[i]
            y = x[-1]
            res[int(y)-1] = x[0:len(x)-1]
        return " ".join(res)
        