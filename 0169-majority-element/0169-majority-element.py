class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dec = dict()


        """
        6
        { 3: 2     2:2   6:9    7:1  }

        3 2 3 2 6 7

        """
        

        for i in nums:
            if i in dec:
                dec[i] += 1
            else:
                dec[i] = 1

        v = 0
        k = 0
        for key, val in dec.items():
            

            if val > v:
                k = key
                v = val

            else:
                continue


        return k



        

                
