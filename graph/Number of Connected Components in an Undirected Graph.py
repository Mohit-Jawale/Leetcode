class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        root = [i for i in range(n)]
        rank = [1]* n
        components = n
        
        
        
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        
        def union(node):
            rootX = find(node[0])
            rootY = find(node[1])
            nonlocal components
            if rootX != rootY:
                if rank[rootX]>rank[rootY]:
                    root[rootY] = rootX
                elif rank[rootY]>rank[rootX]:
                    root[rootX] = rootY
                else:
                    root[rootY]=rootX
                    rank[rootX]+=1
                components-=1  
                
        for i in edges:
            union(i)
        return(components)    
    


        
