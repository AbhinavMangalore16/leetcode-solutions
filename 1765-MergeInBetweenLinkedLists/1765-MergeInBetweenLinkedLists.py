# Last updated: 3/31/2026, 9:33:55 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        p1 = list1
        h1 = list1
        l1,l2 = 0,0
        while (p1.next!=None) and (l1!=a-1):
            p1 = p1.next
            l1+=1
        p2 = p1
        while (p2.next!=None) and (l2!=(b-a+1)):
            p2 = p2.next
            l2+=1
        p1.next = list2
        while(list2.next!=None):
            list2= list2.next
        list2.next = p2.next
        return h1