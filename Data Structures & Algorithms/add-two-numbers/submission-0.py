# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        one = 0
        two = 0
        mult = 1
        while l1:
            add = l1.val * mult
            one += add
            mult *= 10
            l1 = l1.next
        mult = 1
        while l2:
            add = l2.val * mult
            two += add
            mult *= 10
            l2 = l2.next
        added = one+two
        added = str(added)[::-1]
        dummy = ListNode()
        curr = dummy
        for char in added:
            curr.next = ListNode(char)
            curr = curr.next
        return dummy.next