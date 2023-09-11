# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            while stack != [] and stack[-1] < head.val:
                stack.pop()
            stack.append(head.val)
            head = head.next
        data = ListNode()
        value = data
        while stack != []:
            data.next = ListNode(stack.pop(0))
            data = data.next
        return value.next
            
        
            
            
        