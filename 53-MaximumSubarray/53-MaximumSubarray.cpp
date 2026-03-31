// Last updated: 3/31/2026, 9:40:45 PM
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
    int maxsum = nums[0];
    int currsum = nums[0];

    for (int i = 1; i < nums.size(); i++) {
        currsum = max(nums[i], currsum + nums[i]);
        maxsum = max(maxsum, currsum);
    }

    return maxsum;
}
};