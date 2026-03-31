# Last updated: 3/31/2026, 9:28:56 PM
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []
        for i in range((n-k+1)):
            sub = nums[i:i+k]
            freq = Counter(sub)
            sorted_elems = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))
            top_x = {el for el, _ in sorted_elems[:x]}
            total = sum(val for val in sub if val in top_x)
            ans.append(total)
        return ans