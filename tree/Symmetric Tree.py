# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        
        def preorder(n_left,n_right):
            
            if n_left is None and n_right is None:
                return True
            
            if n_left is None or n_right is None:
                return False
    
            if n_left.val != n_right.val:
                return False
            
            ans = True
            ans = preorder(n_left.left,n_right.right) and   preorder(n_left.right,n_right.left)
            print(ans)
            return ans
        
        
        return(preorder(root.left,root.right))
