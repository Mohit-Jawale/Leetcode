# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
            parent_n = None
           
            def depth(node,n):
                nonlocal parent_n
                if not node:
                    return 
                if node.val == n:
                    return 1
                
                ans_left = depth(node.left,n)
                ans_right = depth(node.right,n)
                
                if ans_left==1 or ans_right==1:
                    parent_n = node
                    
                if not ans_left and not ans_right:
                    return 
                elif not ans_left and ans_right:
                    return ans_right + 1
                elif ans_left and not ans_right:
                    return ans_left + 1              
            
            
            a = depth(root,x)
            parent_a = parent_n
            
            b = depth(root,y)
            parent_b = parent_n
            
            if a==b and parent_a != parent_b:
                return True
            else:
                return False
                
