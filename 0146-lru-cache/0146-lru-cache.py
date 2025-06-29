class Node:
    def __init__(self, key=None, val = None):
        self.val = val
        self.key = key
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hash = {}

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        
        prev_element = node.prev
        next_element = node.next

        prev_element.next = next_element
        next_element.prev = prev_element


    def insert(self, node):
        last_element = self.tail.prev
        last_element.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = last_element
        

    def get(self, key: int) -> int:


        if key in self.hash:
            self.remove(self.hash[key])
            self.insert(self.hash[key])
            print("here ", key)
            print(self.tail.prev.val)
            print()
            return self.hash[key].val

        return -1


        

    def put(self, key: int, value: int) -> None:
        cur = Node(key, value)
        if key in self.hash:
            val = self.hash[key]
            self.remove(val)
            del self.hash[key]

        self.insert(cur)
        self.hash[key] = cur
            
        if len(self.hash) > self.cap:
            beginnig = self.head.next
            self.remove(beginnig)
            del self.hash[beginnig.key]

      

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)