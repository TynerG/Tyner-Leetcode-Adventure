# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left_node = head
        right_node = head

        prev_left = None
        position = 1
        while position < left:
            prev_left = left_node
            left_node = left_node.next
            right_node = right_node.next
            position += 1

        while position < right:
            right_node = right_node.next
            position += 1
        right_next = right_node.next

        curr = left_node
        prev = right_next
        while left < right:
            next_node = curr.next
            curr.next = prev  # reversing the pointer

            prev = curr
            curr = next_node
            left += 1

        curr.next = prev
        if not prev_left:
            return curr

        prev_left.next = curr
        return head

