# Last updated: 9/22/2026, 12:02:11 AM
1class Solution:
2    def resultArray(self, nums: List[int], k: int) -> List[int]:
3        n = len(nums)
4        nums = [x % k for x in nums]
5        res = [0] * k
6        for req in range(k):
7            dp = {}
8
9            def solve(i, prevProd):
10                if i >= n:
11                    return 0
12                if (i, prevProd) in dp:
13                    return dp[(i, prevProd)]
14
15                skip = 0
16                take = 0
17                if prevProd == k:
18                    skip = solve(i + 1, k)
19                if prevProd == k:
20                    curProd = nums[i]
21                else:
22                    curProd = (prevProd * nums[i]) % k
23                take += 1 if curProd == req else 0
24                take += solve(i + 1, curProd)
25                dp[(i, prevProd)] = take + skip
26                return dp[(i, prevProd)]
27            res[req] = solve(0, k)
28
29        return res