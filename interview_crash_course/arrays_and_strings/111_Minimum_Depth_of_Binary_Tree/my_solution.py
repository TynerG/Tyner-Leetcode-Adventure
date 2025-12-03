from math import inf
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return inf

            if root.left is None and root.right is None:
                return 1

            left_depth = dfs(root.left)
            right_depth = dfs(root.right)

            return 1 + min(left_depth, right_depth)

        if root is None:
            return 0

        return dfs(root)