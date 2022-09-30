# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    
    def preorder(self,p,q):
        
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        
        if p.val != q.val:
            return False
        ans = True
        ans = self.preorder(p.left,q.left) and self.preorder(p.right,q.right)
    
        
        return ans
            
        
        
        
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        ans = self.preorder(p,q)
        return ans
