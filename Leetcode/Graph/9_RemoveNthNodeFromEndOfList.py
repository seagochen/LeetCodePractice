"""
Given the head of a linked list, 
remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
"""

from typing import Optional
from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        root = ListNode(next=head)
        node = root
        queue = deque(maxlen=n)
        while node and node.next:
            queue.append(node)
            node = node.next
        node_before = queue.popleft()
        node_before.next = node_before.next.next
        return root.next
