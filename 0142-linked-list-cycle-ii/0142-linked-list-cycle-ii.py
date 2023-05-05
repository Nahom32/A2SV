# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        val = set()
        while head:
            if head not in val:
                val.add(head)
                head = head.next
            else:
                return head
            
        
            
        