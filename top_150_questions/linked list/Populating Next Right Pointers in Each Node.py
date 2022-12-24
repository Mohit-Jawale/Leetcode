"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        lookup = collections.deque()

        def add_to_queue(node):
            if not lookup:
                lookup.appendleft(node)
                return None 
            else:
                if lookup[0].right == node:
                    if lookup[0].next !=None:
                        ans = lookup[0].next.left
                        lookup.appendleft(node)
                        return ans
                    else:
                        lookup.appendleft(node)
                        return None    
                else:
                    ans = lookup[0].right
                    lookup.appendleft(node)
                    return ans    

                   

        def preorder(node):
            if node == None:
                return

            next_val = add_to_queue(node)
            node.next = next_val

            preorder(node.left)
            preorder(node.right)
            
        
            lookup.popleft()
        
            return
        preorder(root)
        return root    
              
