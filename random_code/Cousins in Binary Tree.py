# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#### one pass solution 

  def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
            res = []
           
            def cousins(node,parent,depth):
                if not node:
                    return 
                if node.val == x or node.val == y:
                    res.append((depth,parent))
                
                ans_left = cousins(node.left,node,depth+1)
                ans_right = cousins(node.right,node,depth+1)
                
            
            cousins(root,None,0)
            a,b = res
          
            if a[0] == b[0] and a[1]!=b[1]:
                return True
            else:
                return False





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
                
