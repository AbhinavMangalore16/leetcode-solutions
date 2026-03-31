# Last updated: 3/31/2026, 9:33:04 PM
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        c = 0
        for i in operations:
            if i[1] == "-":
                c-=1
            else:
                c+=1
        return c