class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
     
        def dfs(start,end):
            
            stack = [start]
            seen = set()
            
            while stack:
                
                node = stack.pop()
                
                if node == end:
                    return True
                if node in seen:
                    continue
                seen.add(node)
                
                for neighbour in adj_list[node]:
                    stack.append(neighbour)
        
        
        adj_list = [[] for _ in range(n)]
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        
        return(dfs(source,destination))
        
        
 class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:



        def dfs(start,end):
            stack = [start]
            seen = set()
            while stack:
                node = stack.pop(0)
                print(node)
                if node == end:
                    return True
                if node in seen:
                    continue

                seen.add(node)

                for neighbour in adj_list[node]:
                    stack.append(neighbour)


        #### use dict bcz it can contains any nodes
        adj_list = collections.defaultdict(list)

        for i,j in edges:
            adj_list[i].append(j) 
            adj_list[j].append(i)                   

        return dfs(source,destination)       
        
