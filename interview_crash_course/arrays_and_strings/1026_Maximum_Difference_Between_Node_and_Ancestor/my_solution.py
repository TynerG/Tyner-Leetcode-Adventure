# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# improvement: don't even need to calculate the difference at every recursion, just record the
# max and min along each path and do the subtraction when we arrive at the leaf
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs_maxDiff(root: Optional[TreeNode], minAnc: int, maxAnc: int) -> int:
            if root is None:
                return 0

            curr_diff = max(abs(root.val - minAnc), abs(root.val - maxAnc))

            if root.val < minAnc:
                minAnc = root.val

            elif root.val > maxAnc:
                maxAnc = root.val

            left_diff = dfs_maxDiff(root.left, minAnc, maxAnc)
            right_diff = dfs_maxDiff(root.right, minAnc, maxAnc)

            return max(curr_diff, left_diff, right_diff)

        if root is None:
            return 0

        return dfs_maxDiff(root, root.val, root.val)

if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(2)
    root.left = TreeNode(5)
    root.right = TreeNode(0)
    root.right.left = TreeNode(4)
    root.right.left.right = TreeNode(6)
    root.right.left.right.left = TreeNode(1)
    root.right.left.right.left.left = TreeNode(3)

    print(solution.maxAncestorDiff(root))