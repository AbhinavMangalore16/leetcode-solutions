// Last updated: 3/31/2026, 9:39:09 PM
class Solution {
public:
    int rob(vector<int>& nums) {
        int h1 = 0, h2 = 0;
        for (int i = 0;i<nums.size();i++){
            int robb = max(nums[i]+h1, h2);
            h1 = h2;
            h2 = robb;
        }
        return h2;
    }
};