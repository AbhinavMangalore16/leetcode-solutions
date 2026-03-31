# Last updated: 3/31/2026, 9:32:20 PM
class Solution:
    def countOperations(self, n1: int, n2: int) -> int:
        c = 0
        while n1 != 0 and n2 != 0:
            if n1 >= n2:
                c+= n1//n2  
                n1%= n2
            else:
                c+= n2//n1
                n2%= n1
        return c