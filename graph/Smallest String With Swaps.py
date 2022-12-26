class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        n = len(s)
        root = [i for i in range(n)]
        rank = [1]*n

        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]

        def union(x,y):
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                if rank[rootX]> rank[rootY]:
                    root[rootY] = rootX
                elif rank[rootY]> rank[rootX]:
                    root[rootX] = rootY
                else:
                    root[rootY] = rootX
                    rank[rootX]+=1

             

        for i in pairs:
            union(i[0],i[1])

        
        connected = collections.defaultdict(list)

        for i in range(n):
            connected[find(i)].append(s[i])

        
        for stack in connected.values():
            stack.sort(reverse=True)   # sort in reverse order to be able pop smallest from stack in O(1)

        new = "".join([connected[find(i)].pop() for i in range(n)])
        
        return new   
