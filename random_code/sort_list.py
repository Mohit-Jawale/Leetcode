# pay attention to this solution, it is very simple and easy to understand.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def find_middle(head):
            fast_ptr = head.next
            slow_ptr = head
            
            while fast_ptr and fast_ptr.next:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next
            
            return slow_ptr
        
        def merge_sort_ll(head):
            if head == None or head.next == None:
                return head
            
            tail = find_middle(head)
            tmp = tail.next
            tail.next = None
            tail = tmp
            head  = merge_sort_ll(head)
            tail = merge_sort_ll(tail)
            return merge(head,tail)
        
        def merge(left,right):
            newhead = tail = ListNode()
            
            while left and right:
                if left.val < right.val:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                    
                tail = tail.next
                
            if left:
                tail.next = left
            if right:
                tail.next = right
                
            return newhead.next  
        
        return merge_sort_ll(head)
