# Last updated: 3/31/2026, 9:30:18 PM
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        targetIdx, targetLen = 0, len(str2)  
        for currChar in str1:
            if targetIdx < targetLen and (ord(str2[targetIdx]) - ord(currChar)) % 26 < 2:
                targetIdx += 1  
        return targetIdx == targetLen