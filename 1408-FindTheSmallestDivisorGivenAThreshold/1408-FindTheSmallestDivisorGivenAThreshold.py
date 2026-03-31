# Last updated: 3/31/2026, 9:35:00 PM
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        l, h = 1, max(nums)
        res = h
        while l<=h:
            mid = (l+h)//2
            summ = 0
            for i in range(n):
                summ += math.ceil(nums[i]/mid)
            if summ<=threshold:
                res = mid
                h = mid-1
            else:
                l = mid+1
        return res