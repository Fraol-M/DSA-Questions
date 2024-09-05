class Solution:
    def smallestNumber(self, num: int) -> int:
        num = list(str(num))
        
        
        num.sort()
        res = ""
        cnt= 0 
        if num[0] == "-":
            res = "-"
            for i in range(len(num)-1, 0, -1):
                res+=num[i]
            return int(res)
        for i in range(len(num)):
            if num[i] == "0":
                cnt+=1
            elif num[i] != "0":
                res+=num[i]
                if cnt > 0:
                    res = res + ("0" * cnt)
                    cnt = 0
        return int(res) if res != "" else 0






        return 0