# Last updated: 3/31/2026, 9:40:12 PM
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        maxx = 0
        i = 0
        while i < n:
            st = i
            if not stack:
                stack.append((heights[i],i))
            if heights[i]<stack[-1][0]:
                while stack and heights[i]<stack[-1][0]:
                    h_top, i_top = stack.pop()
                    rect = h_top * (i - i_top)
                    maxx = max(maxx, rect)
                    st = i_top
                stack.append((heights[i], st))
            else:
                stack.append((heights[i],i))
            # print(stack)
            i+=1
        while stack:
            h_top, i_top = stack.pop()
            rect = h_top * (n - i_top)
            maxx = max(maxx, rect)
        return maxx

