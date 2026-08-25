# Last updated: 8/25/2026, 11:16:22 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        curr = head
10        st = set()
11        while curr:
12            if curr in st:
13                return True
14            st.add(curr)
15            curr = curr.next
16        return False