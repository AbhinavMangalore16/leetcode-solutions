# Last updated: 3/31/2026, 9:32:42 PM
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        max_fruits = 0
        total = 0
        left = 0

        for right in range(n):
            total += fruits[right][1]

            while left <= right:
                left_pos = fruits[left][0]
                right_pos = fruits[right][0]

                min_steps = min(abs(startPos - left_pos), abs(startPos - right_pos)) + (right_pos - left_pos)
                
                if min_steps <= k:
                    break
                total -= fruits[left][1]
                left += 1

            max_fruits = max(max_fruits, total)

        return max_fruits