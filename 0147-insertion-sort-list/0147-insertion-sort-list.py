# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val = []
        while head:
            val.append(head.val)
            head = head.next
        i = 1
        while i < len(val):
            j = i-1
            temp = val[i]
            while j >= 0 and  val[j] > temp:
                val[j+1] = val[j]
                j-=1
            val[j+1] = temp
            i+=1
        ret = h = ListNode()
        for i in val:
            h.next = ListNode(i)
            h = h.next
        return ret.next
        
            
            
                
        