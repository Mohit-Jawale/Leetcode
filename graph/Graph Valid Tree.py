class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        root = [i for i in range(n)]
        rank = [1]*n
        valid_tree = 0
        components =n
        
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        
        def union(i):
            rootX = find(i[0])
            rootY = find(i[1])
            nonlocal valid_tree
            nonlocal components
            if rootX != rootY:
                if rank[rootX]> rank[rootY]:
                    root[rootY]=rootX
                elif rank[rootX]< rank[rootY]:
                    root[rootX] = rootY
                else:
                    root[rootY] = rootX
                    rank[rootX]+=1  
                components-=1    
            valid_tree+=1

                
        for i in edges:
            union(i)
        
        print(valid_tree)
        print(components)
        if valid_tree == n-1 and components==1:
            return True
        else:
            return False
