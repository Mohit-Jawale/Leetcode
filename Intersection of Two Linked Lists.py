# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        
        ptr_a = headA
        counta = 0
        ptr_b = headB
        countb = 0
        
        while ptr_a or ptr_b:
            if ptr_a:
                ptr_a = ptr_a.next
                counta+=1
            if ptr_b:
                ptr_b = ptr_b.next
                countb+=1
                
        diff = counta- countb

        temp1 = headA 
        temp2 = headB
        if diff<0:
            temp1 = headB
            temp2= headA
        
        temp_count = 0
        while abs(diff) != temp_count:
            temp_count+=1
            temp1 = temp1.next
    
        while temp1 and temp2:
            if temp1 == temp2:
                return temp1
            temp1 =temp1.next
            temp2= temp2.next
            
        if temp1 == temp2:
            return None
        
       
            
        
            
        
