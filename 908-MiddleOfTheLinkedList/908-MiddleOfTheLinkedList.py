# Last updated: 3/31/2026, 9:36:24 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hare = head
        tor = head
        while(hare!=None and hare.next!= None):
            tor = tor.next
            hare = hare.next.next
        return tor