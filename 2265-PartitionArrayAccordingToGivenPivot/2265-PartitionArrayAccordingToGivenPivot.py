# Last updated: 3/31/2026, 9:32:24 PM
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less, high, count = [], [], 0

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                count += 1
            else:
                high.append(num)

        return less + [pivot] * count + high