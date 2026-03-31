# Last updated: 3/31/2026, 9:40:56 PM
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first_occ():
            l, h = 0, len(nums)-1
            first = -1
            while l<=h:
                mid = l + (h-l)//2
                if nums[mid] == target:
                    first = mid
                    h = mid-1
                elif nums[mid]<target:
                    l = mid+1
                else:
                    h = mid-1
            return first
        def last_occ():
            l, h = 0, len(nums)-1
            last = -1
            while l<=h:
                mid = l+(h-l)//2
                if nums[mid] == target:
                    last = mid
                    l = mid+1
                elif nums[mid]<target:
                    l = mid+1
                else: h = mid-1
            return last
        return [first_occ(), last_occ()]