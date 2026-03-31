// Last updated: 3/31/2026, 9:38:35 PM
class Solution {
public:
    int addDigits(int num) {
        if (num==0){
            return 0;
        }
        if (!(num%9)){
            return 9;
        }
        return num%9;
    }
};