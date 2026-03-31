# Last updated: 3/31/2026, 9:33:48 PM
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans_size = ((n - 1) * 2) + 1
        used_nums = set()
        ans = [-1] * ans_size

        def dfs(idx):
            if idx == len(ans):  # Base case: all positions are filled
                return True
            
            if ans[idx] != -1:  # Skip already filled positions
                return dfs(idx + 1)

            for num in range(n, 0, -1):
                if num in used_nums:  # Number already used
                    continue
                if num > 1 and (idx + num >= len(ans) or ans[idx + num] != -1):
                    continue
                
                # Decision
                used_nums.add(num)
                ans[idx] = num
                if num > 1:
                    ans[idx + num] = num

                # Find the next empty position
                j = idx + 1
                while j < len(ans) and ans[j] != -1:
                    j += 1

                # Recursion
                if dfs(j):
                    return True

                # Backtrack
                used_nums.remove(num)
                ans[idx] = -1
                if num > 1:
                    ans[idx + num] = -1

            return False

        dfs(0)
        return ans