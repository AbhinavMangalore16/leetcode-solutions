# Last updated: 3/31/2026, 9:33:40 PM
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0]*len(boxes)
        for curr in range(len(boxes)):
            if boxes[curr] == "1":
                for new_pos in range(len(boxes)):
                    res[new_pos] += abs(new_pos-curr)
        return res