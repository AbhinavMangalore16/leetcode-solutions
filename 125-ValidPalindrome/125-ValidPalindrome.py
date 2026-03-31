# Last updated: 3/31/2026, 9:39:45 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = 0
        high = len(s) - 1
        while low<high:
            while(not s[low].isalnum() and low<high):
                low+=1
            while(not s[high].isalnum() and low<high):
                high-=1
            if (s[low].lower()!=s[high].lower()):
                return False
            low+=1
            high-=1
        return True