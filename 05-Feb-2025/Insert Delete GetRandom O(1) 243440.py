# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        

        self.dic = defaultdict(int)
        self.arr = []
        self.i = 0
        
        
    def insert(self, val: int) -> bool:
        if val not in self.dic:
            self.arr.append(val)
            self.dic[val] = self.i
            self.i+=1
            return True

        return False


    def remove(self, val: int) -> bool:

        if val in self.dic:
            ind_1 = self.dic[val]

            self.dic[self.arr[-1]] = ind_1
            self.arr[ind_1], self.arr[-1] = self.arr[-1], self.arr[ind_1]
            self.i-=1
            self.arr.pop()
            del self.dic[val]
            return True
        return False


    def getRandom(self) -> int:
        ind = randint(0, len(self.arr)-1)
        return self.arr[ind]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()