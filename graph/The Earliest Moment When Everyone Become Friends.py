class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        
    
        root = [i for i in range(n)]
        rank = [1]* n
        components = n
        early_time = -1
        
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        
        def union(node):
            rootX = find(node[1])
            rootY = find(node[2])
            nonlocal components
            nonlocal early_time
            if rootX != rootY:
                if rank[rootX]>rank[rootY]:
                    root[rootY] = rootX
                elif rank[rootY]>rank[rootX]:
                    root[rootX] = rootY
                else:
                    root[rootY]=rootX
                    rank[rootX]+=1
                components-=1  
                if components == 1:
                    early_time = node[0]
        logs.sort()
        for i in logs:
            union(i)
        return(early_time)    
