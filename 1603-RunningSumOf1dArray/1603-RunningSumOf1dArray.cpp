// Last updated: 3/31/2026, 9:34:25 PM
class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        // vector<int> ans;
        // int sum = 0;
        // for(auto i:nums){
        //     sum+=nums[i];
        //     ans.push_back(sum);
        // }
        // return ans;
        int n = nums.size();
        vector<int> ans(n,0);
        ans[0] = nums[0];
        for(int i=1;i<n;i++){
            ans[i] = ans[i-1]+nums[i];
        }
        return ans;
    }
};