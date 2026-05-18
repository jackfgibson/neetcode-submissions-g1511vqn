# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = [root]
        while q:
            l = len(q)
            right = None
            for i in range(l):
                node = q[0]
                q = q[1:]
                if node:
                    right = node
                    q.append(node.left)
                    q.append(node.right)
            if right:
                res.append(right.val)
        return res