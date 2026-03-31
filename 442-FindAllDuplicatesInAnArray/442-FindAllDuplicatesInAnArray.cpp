// Last updated: 3/31/2026, 9:37:53 PM
class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> dup;
        for(auto i:nums){
            if (nums[abs(i)-1]<0){
                dup.push_back(abs(i));
            }
            else{
                nums[abs(i)-1] *= -1;
            }
        }
        return dup;
    }
};