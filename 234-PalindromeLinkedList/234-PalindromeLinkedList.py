# Last updated: 3/31/2026, 9:38:42 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        slow = fast = head
        reversed_list = None
        while fast and fast.next:
            tmp = slow
            slow = slow.next
            fast = fast.next.next
            tmp.next = reversed_list
            reversed_list = tmp

        if fast:
            slow = slow.next

        while reversed_list and reversed_list.val == slow.val:
            reversed_list = reversed_list.next
            slow = slow.next

        return not reversed_list