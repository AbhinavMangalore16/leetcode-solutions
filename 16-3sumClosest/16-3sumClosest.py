# Last updated: 3/31/2026, 9:41:11 PM
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        answer = nums[0]+nums[1]+nums[2]
        for i in range(n-2):
            j = i+1
            k = n-1
            while(j<k):
                summ = nums[i]+nums[j]+nums[k]
                if summ==target:
                    return summ
                elif abs(summ-target) < abs(answer-target):
                    answer = summ
                elif (summ<target):
                    j=j+1
                else:
                    k=k-1
        return answer
