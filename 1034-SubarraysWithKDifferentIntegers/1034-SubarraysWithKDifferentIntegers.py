# Last updated: 3/31/2026, 9:35:58 PM
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
            counts = defaultdict(int)
            total = left = curr = 0

            for right in range(len(nums)):
                num = nums[right]
                counts[num] += 1

                if counts[num] == 1:
                    k -= 1

                while k < 0:
                    left_num = nums[left]
                    counts[left_num] -= 1
                    if counts[left_num] == 0:
                        k += 1
                    left += 1
                    curr = 0

                if k == 0:
                    while counts[nums[left]] > 1:
                        counts[nums[left]] -= 1
                        left += 1
                        curr += 1
                    total += (curr + 1)

            return total