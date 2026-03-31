# Last updated: 3/31/2026, 9:31:14 PM
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        for i in range(len(sentence)-1):
            if sentence[i+1] == ' ':
                if sentence[i] != sentence[i+2]:
                    return False
        return True
