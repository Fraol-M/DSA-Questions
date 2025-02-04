# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        

        dic = defaultdict(list)

        for path in paths:

            
            dire =path.split(" ")
            root_path = dire[0]

            for i in range(1, len(dire)):
                files = dire[i].split("(")
                dic[files[1][:-1]].append(root_path+"/"+files[0])
        

        result = []
        for i, j in dic.items():
            same = []
            if len(j)>1:
                for p in j:
                    same.append(p)

                result.append(same)
        return result
                


           
            


        
