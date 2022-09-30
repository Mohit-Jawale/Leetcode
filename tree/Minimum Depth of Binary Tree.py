# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def depth(node):
            if node is None:
                return 0
            
            left, right = 0 , 0
            left = depth(node.left)
            right = depth(node.right)
            
            print(left,right)
            return (min(left,right) or max(left,right))+1
                
                
        return(depth(root))
