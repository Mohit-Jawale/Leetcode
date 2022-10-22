# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
            def lca(root,p,q):
                if root == None:
                    return None
                if root == p or root == q:
                    return root
                
                left_ans = lca(root.left,p,q)
                right_ans = lca(root.right,p,q)
                
                if left_ans and right_ans:
                    return root
                elif left_ans and right_ans == None:
                    return left_ans
                elif left_ans == None and right_ans:
                    return right_ans
                
            return(lca(root,p,q))
                
                
                    
                
              
            
            
            
            return(lca(root,p,q))
         
          
                
                
                
                
                

            
            
    
            
            
        
        
        
