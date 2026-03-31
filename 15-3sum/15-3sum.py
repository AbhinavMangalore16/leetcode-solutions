# Last updated: 3/31/2026, 9:41:14 PM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i>0 and (nums[i]==nums[i-1]):
                continue
            pairs = self.helper(nums, i+1, -nums[i])
            for p in pairs:
                triplets.append([nums[i]]+p)
        return triplets
    def helper(self, nums: List[int], st: int, tgt: int):
        pairs = []
        l, r = st, len(nums)-1
        while l<r:
            summ = nums[l]+nums[r]
            if summ==tgt:
                pairs.append([nums[l], nums[r]])
                while l<r and nums[l]==nums[l+1]:
                    l+=1
                while l<r and nums[r]==nums[r-1]:
                    r-=1
                l += 1
                r -= 1
            elif summ<tgt:
                l+=1
            else:
                r-=1
        return pairs