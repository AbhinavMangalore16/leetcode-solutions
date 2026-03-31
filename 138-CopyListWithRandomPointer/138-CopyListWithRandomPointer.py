# Last updated: 3/31/2026, 9:39:35 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        COPY = {}
        COPY[None] = None
        curr = head
        while curr:
            new_node = Node(curr.val)
            COPY[curr] = new_node
            curr = curr.next
        curr = head
        while curr:
            copied = COPY[curr]
            copied.next = COPY[curr.next]
            copied.random = COPY[curr.random]
            curr = curr.next
        return COPY[head]