# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        dic = defaultdict(list)
        # aet -
        for s in strs:
            k = "".join(sorted(s))
            dic[k].append(s)
        
        result = []

        for key, values in dic.items():
            result.append(values)
        return result


            



        