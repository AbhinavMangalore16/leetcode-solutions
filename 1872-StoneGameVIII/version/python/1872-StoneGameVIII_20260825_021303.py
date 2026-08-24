# Last updated: 8/25/2026, 2:13:03 AM
1class Solution:
2    def resultArray(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        l1 = [nums[0],]
5        l2 = [nums[1],]
6        for i in range(2,n):
7            if l1[-1]>l2[-1]:
8                l1.append(nums[i])
9            else:
10                l2.append(nums[i])
11        return l1+l2