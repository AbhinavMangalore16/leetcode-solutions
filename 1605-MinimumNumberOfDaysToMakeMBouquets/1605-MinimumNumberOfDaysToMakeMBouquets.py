# Last updated: 3/31/2026, 9:34:23 PM
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def bouquet(mid,n):
            bqs = 0
            flw = 0
            for i in range(n):
                if bloomDay[i]<=mid:
                    flw+=1
                    if flw==k:
                        bqs+=1
                        flw=0
                else:
                    flw = 0
            return bqs>=m

        f = len(bloomDay)
        if ((m*k)>f):
            return -1
        minn = -1
        l, h = min(bloomDay), max(bloomDay)
        while l<=h:
            mid = l + (h-l)//2
            if bouquet(mid,f):
                minn = mid
                h = mid-1
            else:
                l = mid+1
        return minn