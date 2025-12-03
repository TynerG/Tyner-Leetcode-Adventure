# Definition for a binary tree node.
from typing import Tuple, Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# improvements: complexity-wise this is optimal, but could be written in a much readable way.
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> Tuple[bool, Optional['TreeNode']]:
            if root is None:
                return (False, None)

            pq_found = False
            if root.val == p.val or root.val == q.val:
                pq_found = True

            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)

            if left[1] is not None:
                return (True, left[1])
            if right[1] is not None:
                return (True, right[1])

            if left[0] == True and right[0] == True:
                return (True, root)

            if (left[0] == True or right[0] == True) and pq_found:
                return (True, root)

            if left[0] == True or right[0] == True:
                return (True, None)

            if pq_found:
                return (True, None)

            return (False, None)

        return dfs(root, p, q)[1]

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    print(s.lowestCommonAncestor(root, root.left, root.right))