class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        n = len(nums)
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
                if rank[rootX] > rank[rootY]:
                    root[rootY] = rootX
                elif rank[rootY] > rank[rootX]:
                    root[rootX] = rootY
                else:
                    root[rootY] = rootX
                    rank[rootX]+=1

        lookup = {}
 

        for i in range(n):

            if nums[i] in lookup:
                continue

            lookup[nums[i]]= i    

            if nums[i]+1 in lookup:
                union(i,lookup[nums[i]+1])
            if nums[i]-1 in lookup:
                union(i,lookup[nums[i]-1])

        max_dict = collections.defaultdict(list)
        for i in range(n):
            max_dict[find(i)].append(nums[i])
        b=0    
        for i in max_dict:
            a = len(max_dict[i])
            b = max(a,b)
        return b    



   

                
