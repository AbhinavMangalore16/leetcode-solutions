// Last updated: 3/31/2026, 9:41:20 PM
class Solution {
public:
    string intToRoman(int num) {
    string symbols[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    
    string res = "";
    for (int i = 0; i < 13; i++) {
        while (num >= values[i]) {
            res += symbols[i];
            num -= values[i];
        }
    }
    
    return res;
    }
};