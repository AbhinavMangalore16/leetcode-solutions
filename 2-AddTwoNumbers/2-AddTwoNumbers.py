# Last updated: 3/31/2026, 9:41:22 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        main = ListNode()
        curr = main
        while(l1 or l2 or c):
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            j = val1+val2+c
            c = j//10
            curr.next = ListNode(j%10)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return main.next