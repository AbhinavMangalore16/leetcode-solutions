# Last updated: 3/31/2026, 9:41:15 PM
class Solution:
    def intToRoman(self, num: int) -> str:
        romans = ["M", "CM","D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I",]
        numerals = [1000,900, 500, 400, 100, 90, 50, 40, 10, 9, 5,4,1,]
        ROMAN = ""
        for i in range(13):
            while (num>=numerals[i]):
                ROMAN += romans[i]
                num -= numerals[i]
        return ROMAN