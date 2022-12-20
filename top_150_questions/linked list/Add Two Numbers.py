# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l = ListNode(0)
        head = l 
        carry = 0
        while l1!=None or l2!=None:
            if l1!=None and l2!=None:
                value = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1 != None and l2 == None:
                value = l1.val + carry
                l1 = l1.next
            else:
                 value = l2.val + carry
                 l2 = l2.next
            carry= value//10
            num= value%10
            print(num,carry)
            l.val = num
            l.next = ListNode(0)
            l = l.next

        temp = head

        if carry>0:
            l.val = carry
        else:
            prev = None
            while temp.next!= None:
                print(temp.val)
                prev = temp
                temp = temp.next
            prev.next = None  

            
        return head



