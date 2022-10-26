# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        temp = head
        count = 0
        while temp:
            count+=1
            temp=temp.next
        
        if count ==1:
            head = None
            return head
        
        del_n = count - n + 1
        temp = head
        prev = None
        for i in range(1,del_n):
            prev = temp
            temp = temp.next
    
        # remove node
        if prev:
            prev.next = temp.next
            return head
        
        temp = temp.next
        return temp
        
        
            
            
