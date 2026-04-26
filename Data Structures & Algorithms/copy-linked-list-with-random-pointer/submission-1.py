"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        oldNew = {}
        curr = head
        while curr:
            oldNew[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            new = oldNew[curr]
            new.next = oldNew.get(curr.next)
            new.random = oldNew.get(curr.random)
            curr = curr.next
        return oldNew[head]