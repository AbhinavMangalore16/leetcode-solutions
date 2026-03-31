// Last updated: 3/31/2026, 9:31:33 PM
#define faster \
ios::sync_with_stdio(false);\
cout.tie(NULL);\
cin.tie(NULL);

class Solution {
public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) {
        faster;
        int maxx = -1, minn = -1, bound = -1;
        long long int res = 0;
        for (int i=0;i<nums.size();i++){
            if ((nums[i]>maxK) || (nums[i]<minK)){
                bound=i;
            }
            if (nums[i]==minK){
                minn = i;
            }
            if (nums[i]==maxK){
                maxx = i;
            }
            res += max(0, min(maxx,minn)-bound);
        }
        return res;
    }
};