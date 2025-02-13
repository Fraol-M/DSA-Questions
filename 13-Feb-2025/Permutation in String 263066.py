# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        res = defaultdict(int)
        count = Counter(s1)
        left = 0
        for i in range(len(s2)):
            res[s2[i]]+=1

            if (i-left)+1 == len(s1):
                if res == count:
                    return True
                res[s2[left]]-=1
                if res[s2[left]] == 0:
                    del res[s2[left]]
                left+=1

        return False
