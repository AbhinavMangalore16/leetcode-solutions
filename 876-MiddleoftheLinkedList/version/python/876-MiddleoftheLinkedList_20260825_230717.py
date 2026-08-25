# Last updated: 8/25/2026, 11:07:17 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        tor = head
9        hare = head
10        while hare and hare.next:
11            tor = tor.next
12            hare = hare.next.next
13        return tor