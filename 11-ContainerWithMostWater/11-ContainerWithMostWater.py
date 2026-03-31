# Last updated: 3/31/2026, 9:41:19 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxx = 0
        l, h = 0,len(height)-1
        while l<=h:
            ar = min(height[l], height[h])*(h-l)
            maxx = max(ar, maxx)
            if height[l]<=height[h]:
                l+=1
            else:
                h-=1
        return maxx