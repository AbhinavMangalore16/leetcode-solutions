# Last updated: 9/4/2026, 2:28:32 AM
1class Solution:
2    def uniformArray(self, nums1: list[int]) -> bool:
3        minn = float('inf')
4        isOdd = False
5        for i in range(len(nums1)):
6            if nums1[i]<minn:
7                minn = nums1[i]
8            if nums1[i]&1:
9                isOdd = True
10        if minn&1:
11            return True
12        return not isOdd
13