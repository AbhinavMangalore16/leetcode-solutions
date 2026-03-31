# Last updated: 3/31/2026, 9:38:46 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n= len(nums)
        majI, majII = None, None
        CI,CII = 0,0
        for i in range(len(nums)):
            if nums[i]==majI:
                CI+=1
            elif nums[i]==majII:
                CII+=1
            elif not CI:
                majI = nums[i]
                CI=1
            elif not CII:
                majII = nums[i]
                CII=1
            else:
                CI-=1
                CII-=1
        l = []
        if majI is not None and nums.count(majI)>n//3:
            l.append(majI)
        if majII is not None and nums.count(majII)>n//3:
            l.append(majII)
        return l
        