# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        

        answers.sort()

        res = 0
    
        left = 0
        count = Counter(answers)

        print(count)

        for i, j in count.items():

            val = i+1
            if val <= j:
                div = j // val
                rem = j % val

                if rem:
                    rem = val

              
                res = res + (div * val) + (rem)
            else:
                res += val
            


            # val = i+1
            # total = i * j

            # k = total // val
            # rem = total % val
            
            # res = res + (k*val) + (rem * val)

        return res