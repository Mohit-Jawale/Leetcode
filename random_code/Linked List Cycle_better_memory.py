# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# this solution is imporved version of last one!!!!
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head == None:
            return False
        
    
        fast_ptr = head
        slow_ptr = head
        
        while fast_ptr!=None and fast_ptr.next!=None:
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
                if fast_ptr == slow_ptr:
                    break
            
        
        if fast_ptr == slow_ptr and fast_ptr.next!=None:
            return True
        else:
            return False
       
