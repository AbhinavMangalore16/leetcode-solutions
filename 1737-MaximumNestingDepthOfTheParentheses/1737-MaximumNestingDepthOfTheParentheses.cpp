// Last updated: 3/31/2026, 9:33:59 PM
class Solution {
public:
    int maxDepth(string s) {
        int maxd = 0, d= 0;
        for (auto i: s){
            if (i =='('){
                d+=1;
                maxd = max(d,maxd);
            }
            else if (i==')'){
                d-=1;
            }
        }
        return maxd;
    }
};