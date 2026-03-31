# Last updated: 3/31/2026, 9:39:10 PM
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        l = list(map(str, nums))
        l.sort(key = lambda x: x*10, reverse=True)
        if l[0] == "0":
            return "0"
        maxx = ''.join(l)
        return maxx