# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        start = 0
        end = len(nums)-1     
        

        def divide_conq(start,end):

            if start>end:
                return

            pivot = (start+end)//2

            root = TreeNode(nums[pivot])

            root.left = divide_conq(start,pivot-1)
            root.right = divide_conq(pivot+1,end)

            return root

        return divide_conq(start,end)
