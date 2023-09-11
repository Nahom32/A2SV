# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev,succ = ListNode(next=head),head
        hold = prev
        while succ:
            if succ.val == val:
                succ = succ.next
                prev.next = succ
            else:
                succ = succ.next
                prev = prev.next
        return hold.next
            