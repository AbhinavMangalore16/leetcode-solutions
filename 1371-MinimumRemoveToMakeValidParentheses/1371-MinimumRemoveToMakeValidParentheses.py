# Last updated: 3/31/2026, 9:35:12 PM
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        invalid_indices = set()
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if not stack:
                    invalid_indices.add(i)
                else:
                    stack.pop()

        invalid_indices.update(stack)
        result = []
        for i, char in enumerate(s):
            if i not in invalid_indices:
                result.append(char)

        return ''.join(result)        