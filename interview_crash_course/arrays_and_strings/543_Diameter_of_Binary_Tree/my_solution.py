from typing import Tuple, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter_dfs(root: Optional[TreeNode]) -> Tuple[int, int]:
            if root is None:
                return (0, 0)

            if root.left is None and root.right is None:
                return (1, 0)

            left_diameter = diameter_dfs(root.left)
            right_diameter = diameter_dfs(root.right)

            leaf_path_len = 1 + max(left_diameter[0], right_diameter[0])
            max_path_len = max(left_diameter[0] + right_diameter[0], left_diameter[1], right_diameter[1])

            return (leaf_path_len, max_path_len)

        return diameter_dfs(root)[1]