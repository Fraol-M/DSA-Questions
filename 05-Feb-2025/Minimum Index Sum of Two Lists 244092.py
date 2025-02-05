# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:


        word_count = defaultdict(int)


        for i in range(len(list1)):
            word_count[list1[i]] = i

        

        k = float("inf")
        result = []

        # 3, 
        for j in range(len(list2)):
            cur = list2[j]

            if cur in word_count:
                ind = word_count[cur]
                _sum = ind+j

                if k > _sum:
                    while result:
                        result.pop()
                    result.append(cur)
                    k = _sum
                elif k == _sum:
                    result.append(cur)
        return result




        return res


        
        