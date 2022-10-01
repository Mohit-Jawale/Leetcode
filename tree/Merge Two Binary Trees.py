# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
       
        def dfs(p,q):
          
            if p is None:
                return q
            if q is None:
                return p
            
            p.val += q.val
            
            p.left = dfs(p.left,q.left)
            p.right = dfs(p.right,q.right)
            

            return p
        
        return(dfs(root1,root2))
