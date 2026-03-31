// Last updated: 3/31/2026, 9:40:42 PM
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        vector<int> freq(n,0);
        freq[0] = 1;
        for(int i=0;i<n-1;i++){
            if (freq[i]==0){
                return false;
            }
            for(int j=i;j<=min(i+nums[i],n-1);j++){
                freq[j]++;
            }
        }
        if (freq[n-1]==0){
            return false;
        }
        else{
            return true;
        }
    }
};