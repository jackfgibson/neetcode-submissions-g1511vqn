# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(curr, big):
            if not curr:
                return 0
            if curr.val >= big:
                big = curr.val
                return 1 + dfs(curr.left, big) + dfs(curr.right, big)
            else:
                return dfs(curr.left, big) + dfs(curr.right, big)
        return dfs(root, root.val)