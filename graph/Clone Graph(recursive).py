"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        
        seen = {}
        
        def dfs(node):
            
            nonlocal seen
            
            if not node:
                return node
            
            if node in seen:
                return seen[node]
            
            
            clone_node = Node(node.val,[])
            
            seen[node] = clone_node
            
            if node.neighbors:
                clone_node.neighbors = [dfs(i) for i in node.neighbors]
                
            return clone_node    
                
        return(dfs(node))
