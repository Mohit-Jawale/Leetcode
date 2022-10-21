# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head == None:
            return False
        
        temp = head
        list_node = set()
        
        while temp and temp not in list_node:
            list_node.add(temp)
            temp = temp.next
            
        
        if temp == None:
            return False
        else:
            return True
        
