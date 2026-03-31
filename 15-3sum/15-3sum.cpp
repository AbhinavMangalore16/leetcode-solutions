// Last updated: 3/31/2026, 9:41:17 PM
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        if (nums.size()<3){
            return {};
        }
        if (nums[0]>0){
            return {};
        }
        vector<vector<int>> res;
        for(int i=0;i< nums.size()-1;i++){
            if (i > 0 && nums[i] == nums[i - 1])
                continue;
            int st = i+1;
            int end = nums.size()-1;
            while(st<end){
                if (nums[i]+nums[st]+nums[end]==0){
                    res.push_back({nums[i],nums[st],nums[end]});
                    while(st<end && nums[st]==nums[st+1]){
                        st++;
                    }
                    while(st<end && nums[end]==nums[end-1]){
                        end--;
                    }
                    st++;
                    end--;
                }
                else if (nums[i]+nums[st]+nums[end]>0){
                    end--;
                }
                else{
                    st++;
                }
            }
        }
        return res;
    }
};