class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        stack = [(0,[0])]
        adj_list = {}
        
        for i in range(len(graph)):
            adj_list[i] = graph[i]
            
        output = []
        
        while stack:
            node, path = stack.pop()

            if node == len(graph)-1:
                output.append(path)
                
            for neigh in adj_list[node]:
                stack.append((neigh,path+[neigh]))
                
        return(output)
        
        
