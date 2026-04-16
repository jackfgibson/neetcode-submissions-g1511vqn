# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #L @ dummy node before start
        #R @ n+1 node
        #move pointers til R 
        #L.next = R
        dummy = ListNode()
        dummy.next = head
        l = dummy
        r = head
        for i in range(n):
            r = r.next
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next
        return dummy.next