# Last updated: 3/31/2026, 9:39:32 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        hare = head 
        tor = head
        while(hare.next and hare.next.next):
            hare = hare.next.next
            tor = tor.next
        second_mid = tor.next
        tor.next = None
        
        prev = None
        curr = second_mid
        while(curr):
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        
        first_mid = head
        while first_mid and prev:
            erste = first_mid.next
            zweite = prev.next
            first_mid.next = prev
            prev.next = erste
            first_mid = erste
            prev = zweite

