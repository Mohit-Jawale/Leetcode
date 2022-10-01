# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        sum = 0
        def dfs(node):
            if node is None:
                return 0
            
            nonlocal sum
            left = dfs(node.left)
            right = dfs(node.right)
            
            sum += abs(left-right)
            
            return left+right+node.val
            
        dfs(root)
        return sum
