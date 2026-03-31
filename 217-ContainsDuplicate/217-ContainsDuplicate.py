# Last updated: 3/31/2026, 9:38:55 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashed = set()
        for n in nums:
            if n in hashed:
                return True
            hashed.add(n)
        return False