# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        curr_root = root
        curr_closest = root.val
        while curr_root is not None:
            if abs(curr_closest - target) > abs(curr_root.val - target):
                curr_closest = curr_root.val
            elif abs(curr_closest - target) == abs(curr_root.val - target):
                curr_closest = min(curr_closest, curr_root.val)
            if curr_root.val > target:
                curr_root = curr_root.left
            elif curr_root.val < target:
                curr_root = curr_root.right
            else:
                return curr_root.val

        return curr_closest