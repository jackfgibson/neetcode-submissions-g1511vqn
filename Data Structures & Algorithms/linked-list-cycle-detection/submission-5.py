# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        if fast:
            fast = fast.next
        else:
            return False

        while slow and fast:
            if slow == fast: return True
            if slow.next and fast.next:
                slow = slow.next
                fast = fast.next.next
            else:
                return False

        return False