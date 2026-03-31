# Last updated: 3/31/2026, 9:34:14 PM
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr) - 1
        while l<= r:
            mid = (l + r) // 2
            missing = arr[mid] - (mid + 1)
            if missing < k:
                l = mid + 1
            else:
                r = mid - 1
        return l + k
