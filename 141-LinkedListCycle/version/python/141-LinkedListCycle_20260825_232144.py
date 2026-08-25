# Last updated: 8/25/2026, 11:21:44 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        tor = head
10        har = head
11        while har and har.next:
12            tor = tor.next
13            har = har.next.next
14            if har is tor:
15                return True
16        return False
17            