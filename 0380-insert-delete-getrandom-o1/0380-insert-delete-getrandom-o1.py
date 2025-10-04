class RandomizedSet:

    def __init__(self):

        self.map = {}
        self.arr = []
    
    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.map:
            ind = self.map[val]
            self.map[self.arr[-1]] = ind
            self.map[self.arr[ind]] = len(self.arr) -1
            
            self.arr[ind], self.arr[-1] = self.arr[-1], self.arr[ind]
            self.arr.pop()
            del self.map[val]
            return True
        return False
    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()