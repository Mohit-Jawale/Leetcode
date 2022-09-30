# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = []
        queue.append(root)
        level_no = 1
        output = []
        while queue:
            
            level = []
            
            for i in range(len(queue)):
                
                node = queue.pop(0)
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                        
            if level_no%2 == 0:
                level.reverse()
            level_no+=1
            if level:
                output.append(level)
            
        print(output)
        return output
             
                
                
                
        
