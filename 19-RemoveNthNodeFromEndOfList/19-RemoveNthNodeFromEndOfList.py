# Last updated: 3/31/2026, 9:41:09 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        bk = dummy 

        for i in range(n+1):
            curr = curr.next
        while curr:
            curr = curr.next
            bk = bk.next
        bk.next = bk.next.next
        return dummy.next