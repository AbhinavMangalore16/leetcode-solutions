# Last updated: 3/31/2026, 9:32:06 PM
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        finding = ["999","888","777","666","555","444","333","222","111","000"]
        for i in finding:
            if i in num:
                return i
        return ""