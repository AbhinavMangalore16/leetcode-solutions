# Last updated: 3/31/2026, 9:29:01 PM
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pq = [(val, i) for i, val in enumerate(nums)]
        heapify(pq)

        for _ in range(k):
            _, i = heappop(pq)
            nums[i] *= multiplier
            heappush(pq, (nums[i], i))

        return nums