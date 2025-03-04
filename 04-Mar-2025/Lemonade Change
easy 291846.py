# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        amount = 0

     
        five = 0 # 1 1
        ten = 0 # 
        twen = 0 # 1


        for i in range(0, len(bills)):
            x = bills[i]
            if x == 5:
                five+=1
            elif x == 10:
                if five >= 1:
                    five-=1
                    ten+=1
                else:
                    return False
            else:
                if (ten >= 1 and five >=1):
                    ten-=1
                    five-=1
                    twen+=1
                elif five>= 3:
                    five-= 3
                else:
                    return False
        return True
        

        