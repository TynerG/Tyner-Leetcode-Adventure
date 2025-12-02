# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast:
            # at the tail
            if fast.next is None:
                return slow

            # at second last
            if fast.next.next is None:
                return slow.next

            fast = fast.next.next
            slow = slow.next