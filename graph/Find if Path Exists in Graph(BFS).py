class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
     
     
        def bfs(start,end):
            
            queue = collections.deque([start])
            seen = set([start])
            
            while queue:
                node = queue.popleft()
                
                if node == end:
                    return True
                
                for neighbour in adj_list[node]:
                    if neighbour not in seen:
                        seen.add(neighbour)
                        queue.append(neighbour)
            return False            
            
        
        
        
        adj_list = [[] for _ in range(n)]
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        
        return(bfs(source,destination))
        
