# Last updated: 3/31/2026, 9:34:54 PM
class Solution:
    def maximum69Number(self, num: int) -> int:
        listy = list(str(num))
        for i in range(len(listy)):
            if listy[i] == "6":
                listy[i] = "9"
                break
        return int("".join(listy))