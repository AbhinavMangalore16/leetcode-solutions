// Last updated: 3/31/2026, 9:39:07 PM
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int hamm = 0;
        while(n!=0){
            n = n & (n-1);
            hamm++;
        }
        return hamm;
    }
};