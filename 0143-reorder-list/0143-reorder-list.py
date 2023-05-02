# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        sec = head
        nodes = []
        while sec != None:
            nodes.append(sec)
            sec = sec.next
        if len(nodes) < 2:
            return head
        l = 0
        if len(nodes)%2 == 0:
            l = len(nodes)//2 - 1
        else:
            l = len(nodes)//2
        counter = 0
        val = head.next
        while counter <= l:
            val = head.next
            head.next = nodes.pop()
            head = head.next
            head.next = val
            head = head.next
            counter+=1
            
        head = head.next
        head.next = None
        
        
            
        
        
        
        