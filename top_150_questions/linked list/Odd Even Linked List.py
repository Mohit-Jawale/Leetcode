# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        if head==None or head.next==None or head.next.next == None :
            return head 
 
        even_head = None
    
        def remove(prev,node):
            prev.next = node.next
            node.next = None

        def attach_to_even_list(prev,curr):
            nonlocal even_head
            if even_head == None:
                even_head = curr
            else:
                prev.next = curr


        curr = head
        next = head.next
        prev = None
        while next and next.next:
            remove(curr,next)
            attach_to_even_list(prev,next)
            prev = next
            curr = curr.next
            if curr:
                next = curr.next
            else:
                next = None    
        
        
        if not next:
            #odd
            curr.next = even_head

        else:
            #even
            curr.next = even_head
            prev.next = next
            
                    

        return head

        
             
