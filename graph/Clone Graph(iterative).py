"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        
        def dfs(node):
            clone_graph = Node(val = node.val)
            stack = [(node,clone_graph)]
            seen = set()
            curr_stack_items = {}
            curr_stack_items[1] = clone_graph
            while stack:
                node_temp,temp_clone_graph = stack.pop()
                if node_temp.val in seen:
                    continue
                seen.add(node_temp.val)
                
                i = 0
                for neigh in (node_temp.neighbors):
                    if neigh.val not in curr_stack_items:
                        curr_stack_items[neigh.val] = Node(neigh.val)
                        temp_clone_graph.neighbors.append(curr_stack_items[neigh.val])
                        stack.append((neigh,temp_clone_graph.neighbors[i]))
                    
                    elif neigh.val in curr_stack_items:
                        temp_clone_graph.neighbors.append(curr_stack_items[neigh.val])
                        stack.append((neigh,temp_clone_graph.neighbors[i]))
                    i+=1
                        
                          
                        
            return clone_graph        
                    
        
        if node is None:
            return node
        
        a = dfs(node)
        return a
