# Last updated: 3/31/2026, 9:38:20 PM
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        hare = nums[0]
        while (tortoise != hare):
            tortoise = nums[tortoise]
            hare = nums[hare]
        return tortoise 