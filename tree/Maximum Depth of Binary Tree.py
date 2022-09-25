# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root is None:
            return 0
        
        left_max = self.maxDepth(root.left)
        left_max+=1
        right_max = self.maxDepth(root.right)
        right_max+=1
        
        return max(left_max,right_max)
        
