# Last updated: 3/31/2026, 9:37:10 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head
        count = 0 
        while curr:
            count +=1
            curr = curr.next
        p, ex = divmod(count, k)
        curr = head 
        res = []
        for i in range(k):
            pthead = curr
            for j in range(p-1+(i<ex)):
                if curr:
                    curr = curr.next
            if curr:
                nnode = curr.next
                curr.next = None
                curr = nnode
            res.append(pthead)
        return res