# Last updated: 3/31/2026, 9:38:57 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        curr = head
        while(curr!=None):
            nxt = curr.next
            curr.next = previous
            previous = curr
            curr = nxt
        return previous