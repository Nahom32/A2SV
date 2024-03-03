# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return None
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        if vals:
            vals.pop(-n)
        if vals:
            head = ListNode(vals[0])
        else:
            return None
        change = head
        for i in range(1,len(vals)):
            change.next = ListNode(vals[i])
            change = change.next
        return head
        
                
                
            
        
        
