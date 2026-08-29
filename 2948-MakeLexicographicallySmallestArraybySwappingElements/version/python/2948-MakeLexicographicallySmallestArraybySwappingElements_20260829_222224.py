# Last updated: 8/29/2026, 10:22:24 PM
1class Solution:
2    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
3        n = len(nums)
4        sorted_nums = sorted(nums)
5        group = {}
6        groupId = {}
7        pos = {}
8        id = 1
9        group[id] = [sorted_nums[0]]
10        groupId[sorted_nums[0]] = id
11
12        for i in range(1, n):
13            if sorted_nums[i] - sorted_nums[i - 1] > limit:
14                id += 1
15
16            group.setdefault(id, []).append(sorted_nums[i])
17            groupId[sorted_nums[i]] = id
18        for i in range(n):
19            grp = groupId[nums[i]]
20            p = pos.get(grp, 0)
21
22            nums[i] = group[grp][p]
23            pos[grp] = p + 1
24
25        return nums