# Last updated: 8/25/2026, 2:44:46 AM
1class Solution:
2    def largestInteger(self, nums: List[int], k: int) -> int:
3        n = len(nums)
4        if k==n:
5            return max(nums)
6        if k==1:
7            d = {}
8            for num in nums:
9                d[num] = d.get(num,0)+1
10            res = -1
11            for num,ct in d.items():
12                if ct ==1:
13                    res = max(res,num)
14            return res
15        res = -1
16        d = {}
17        for num in nums:
18            d[num] = d.get(num,0)+1
19        if d[nums[0]]==1:
20            res= max(res,nums[0])
21        if d[nums[-1]]==1:
22            res= max(res, nums[-1])
23        return res
24        
25