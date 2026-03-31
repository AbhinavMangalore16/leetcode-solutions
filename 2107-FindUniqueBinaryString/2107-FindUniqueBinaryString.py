# Last updated: 3/31/2026, 9:33:07 PM
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res=[]
        for i in range(0, len(nums)):
            if nums[i][i]=='0':
                res.append('1')
            else:
                res.append('0')

        return "".join(res)