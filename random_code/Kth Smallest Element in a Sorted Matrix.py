import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        count = k
        heap = []
        for i in matrix:
            heap = heap+i
            
        heapq.heapify(heap)
        for i in range(1,k):
            print(heapq.heappop(heap))
            
        return (heapq.heappop(heap))   
           
        
          
