# Last updated: 9/13/2026, 10:30:52 PM
1class Solution:
2    def largestNumber(self, nums: List[int]) -> str:
3        l = [str(i) for i in nums]
4        def comp(l1: str, l2: str)-> int:
5            if (l2+l1)>(l1+l2):
6                return 1
7            elif (l2+l1)<(l1+l2):
8                return -1
9            else:
10                return 0
11        l.sort(key=cmp_to_key(comp))
12        if l[0]=="0":
13            return "0"
14        return "".join(l)