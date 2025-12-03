# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        curr_level_sum = 0

        while queue:
            curr_depth_num = len(queue)
            curr_level_sum = 0
            for i in range(curr_depth_num):
                node = queue.popleft()
                curr_level_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return curr_level_sum