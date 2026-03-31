# Last updated: 3/31/2026, 9:30:26 PM
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        L1 = []
        L2 = []
        l = 0
        r = 0
        c = 0 
        while r < len(nums):
            heapq.heappush(L1, (nums[r], r))
            heapq.heappush(L2, (-nums[r], r))
            while l< r and -L1[0][0] - L2[0][0]>2:
                l+=1
                while L1 and L1[0][1]<l:
                    heapq.heappop(L1)
                while L2 and L2[0][1]<l:
                    heapq.heappop(L2)
            c += (r-l+1)
            r+=1
        return c