class heap:
    def __init__(self):
        self.heap = []
        self.heap_count=0
        
    def get_root(self,node_value):
        if node_value%2 == 0:
            return  (node_value-2)//2
        else:
            return (node_value-1)//2
    
    def create_min_heap(self,num):
        if self.heap_count == 0:
            self.heap.append(num)
            self.heap_count+=1
        else:
            self.heap.append(num)
            self.heap_count+=1
            temp_root = -1
            while temp_root != 0:
                temp_root = self.get_root(self.heap.index(num))
                temp_index =self.heap.index(num)
                if self.heap[temp_root]> self.heap[temp_index]:
                    temp_value = self.heap[temp_root]
                    self.heap[temp_root] = self.heap[temp_index]
                    self.heap[temp_index] = temp_value
                else:
                    break
            
            
                
    
    

h = heap()

h.create_min_heap(5)
h.create_min_heap(10)
h.create_min_heap(8)
h.create_min_heap(12)
h.create_min_heap(6)
h.create_min_heap(3)
h.create_min_heap(9)
h.create_min_heap(0)
print(h.heap)
