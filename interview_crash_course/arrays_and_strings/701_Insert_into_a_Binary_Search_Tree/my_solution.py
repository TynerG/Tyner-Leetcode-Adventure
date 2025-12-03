# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# improvement: no need to check if root.left and root.right is None. We can assign the return value
# of insertIntoBST to them directly because we are only returning the input root node no matter what
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        if root.val > val:
            if root.left is None:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)

        elif root.val < val:
            if root.right is None:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)

        return root