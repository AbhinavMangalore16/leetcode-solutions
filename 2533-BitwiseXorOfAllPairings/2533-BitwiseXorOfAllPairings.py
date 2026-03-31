# Last updated: 3/31/2026, 9:31:27 PM
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1 = 0
        xor2 = 0 
        if len(nums1)%2:
            for i in nums2:
                xor2^=i
        if len(nums2)%2:
            for i in nums1:
                xor1^=i
        return xor1^xor2