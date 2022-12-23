class Node:
    def __init__(self,key,value):
        self.key = key 
        self.value = value 
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}

        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.move_node_to_head(node)
            return node.value    

    def move_node_to_head(self,node) :
        self.remove(node)
        self.add_to_head(node)

    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev  

    def add_to_head(self,node):
        node.prev =self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_node_to_head(node)
        else:
            node = Node(key,value)
            self.cache[key] = node
            self.add_to_head(node)
            if len(self.cache)>self.capacity:
                self.remove_from_tail()    
        
    def remove_from_tail(self):
        node = self.tail.prev
        self.remove(node)
        del self.cache[node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
