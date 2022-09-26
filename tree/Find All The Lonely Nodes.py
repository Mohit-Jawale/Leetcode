# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.output = []
    def getLonelyNodes(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
    
        if root is None:
            return
        elif root.left is not None and root.right is  None:
            self.output.append(root.left.val) 
        elif root.left is None and root.right is not None:
            self.output.append(root.right.val)   
        
        
        self.getLonelyNodes(root.left)
        self.getLonelyNodes(root.right)

        return self.output
            
    
        
        
