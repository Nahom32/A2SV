# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        holder = []
        if head == None:
            return head
        while head != None:
            holder.append(head.val)
            head = head.next
        i = 0
        while i < k%len(holder):
            holder.insert(0,holder.pop())
            i+=1
        head=fir = ListNode()
        print(holder)
        for i in holder:
            fir.next = ListNode(i)
            fir = fir.next
        return head.next
        
        