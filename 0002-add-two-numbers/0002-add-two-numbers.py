# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = l1
        current2 = l2
        result = ListNode(0)
        retHead = result
        remainder = 0
        while current1!= None and current2 != None:
            if current1.val + current2.val + remainder >= 10:
                result.val = (current1.val + current2.val + remainder)%10
                remainder = 1
            else:
                result.val = current1.val + current2.val + remainder
                remainder = 0
            current1 = current1.next
            current2 = current2.next
            if current1 != None and current2 != None:
                result.next = ListNode(0)
                result = result.next
        while current2 != None:
            result.next = ListNode((current2.val + remainder)%10)
            if (current2.val + remainder) < 10:
                remainder = 0
            else:
                remainder = 1
            current2 = current2.next
            result = result.next
        while current1 != None:
            result.next = ListNode((current1.val + remainder)%10)
            if (current1.val + remainder) < 10:
                remainder = 0
            else:
                remainder = 1
            current1 = current1.next
            result = result.next
        if remainder == 1:
            result.next = ListNode(1)
        
        return retHead
        
        
                
            
                
            
        
        
        