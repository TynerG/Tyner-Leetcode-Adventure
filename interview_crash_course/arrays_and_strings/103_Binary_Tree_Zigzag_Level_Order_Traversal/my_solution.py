from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque([root])
        zigzag = True
        traversal = []
        while queue:

            curr_level_len = len(queue)
            if zigzag:
                traversal.append([x.val for x in list(queue)])
            else:
                traversal.append([x.val for x in reversed(list(queue))])

            zigzag = not zigzag

            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return traversal