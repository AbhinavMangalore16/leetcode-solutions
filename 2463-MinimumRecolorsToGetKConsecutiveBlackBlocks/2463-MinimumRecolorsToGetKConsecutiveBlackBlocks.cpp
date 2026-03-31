// Last updated: 3/31/2026, 9:31:54 PM
class Solution {
public:
    int minimumRecolors(string blocks, int k) {
        int curr = 0;
        for(int i =0;i<k;i++){
            if (blocks[i]=='W'){
                curr++;
            }
        }
        int minn = curr;
        for(int j=k;j<blocks.length();j++){
            if (blocks[j]=='W'){
                curr++;
            }
            if (blocks[j-k]=='W'){
                curr--;
            }
            minn = min(curr,minn);
        }
        if (minn==-1){
            minn = 0;
        }
        return minn;
    }
};