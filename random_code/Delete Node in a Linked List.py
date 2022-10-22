# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        curr = node
        nextt = curr.next
        prev = None
        while nextt:
            temp_val = curr.val
            curr.val = nextt.val
            nextt.val = temp_val
            prev= curr
            curr = curr.next
            nextt = curr.next
        
            
        prev.next = None    
            

        
