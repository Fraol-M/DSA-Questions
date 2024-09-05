class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:

        ans = 0

        res = 0
        cnt = 0
        for i in range(len(flips)):
            cnt+=i+1
            ans+=flips[i]
            if cnt == ans:
                res+=1
        print(res)
        return res

        