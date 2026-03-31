# Last updated: 3/31/2026, 9:28:43 PM
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        while True:
            mpp = {}
            temp = 0
            for num in nums:
                mpp[num] = mpp.get(num, 0) + 1
                if mpp[num] == 2:
                    temp += 1
            if temp == 0:
                break
            nums = nums[min(3, len(nums)):]
            cnt += 1
        return cnt