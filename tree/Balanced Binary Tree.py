# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        ans = True
        output = []
        def inorder(node):
            if node is None:
                return 0
            nonlocal ans
            nonlocal output
    
            height_left = inorder(node.left)
            height_right = inorder(node.right)
            
            if abs(height_left-height_right)<=1:
                ans = True
                output.append(ans)
            else:
                ans = False
                output.append(ans)
            
            return max(height_left,height_right)+1
            
        inorder(root)
        if False in output:
            return False
        return True
    
