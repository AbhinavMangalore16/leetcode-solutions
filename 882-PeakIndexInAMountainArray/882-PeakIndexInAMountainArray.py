# Last updated: 3/31/2026, 9:36:37 PM
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        N = len(arr)
        l,r = 0, N-1
        while l<r:
            mid = l + (r-l)//2
            if arr[mid]<arr[mid+1]:
                l = mid+1
            else:
                r = mid
        return l