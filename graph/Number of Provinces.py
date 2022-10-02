class Solution:
    

 
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        size = len(isConnected)
        print(size)
        root = [i for i in range(size)]
        print(root)
        rank = [1]*(size)
        provinces =size
        
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]

        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            nonlocal provinces
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    root[rootY] = root[rootX]
                elif rank[rootY] > rank[rootX]:   
                    root[rootX] = root[rootY]
                else:
                    root[rootY] = rootX
                    rank[rootX]+=1
                provinces-=1    
                 


    
    
        for i in range(size):
            for j in range(size):
                if isConnected[i][j]==1 and i<=j:
                    union(i,j)
                    print(i,j)
        print(provinces)
        print(rank)
        print(root)
        return provinces
        
