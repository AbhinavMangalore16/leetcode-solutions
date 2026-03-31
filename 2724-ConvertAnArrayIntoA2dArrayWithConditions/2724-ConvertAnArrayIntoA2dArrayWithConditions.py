# Last updated: 3/31/2026, 9:30:41 PM
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d2 = [[]]
        for i in range(len(nums)):
            j = 0
            while j<len(d2) and nums[i] in d2[j]:
                j+=1
            if j==(len(d2)):
                d2.append([nums[i]])
            else:
                d2[j].append(nums[i])
        return d2