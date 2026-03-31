// Last updated: 3/31/2026, 9:31:09 PM
class Solution {
public:
    int longestSquareStreak(vector<int>& nums) {
        map<int,int> d;
        sort(nums.begin(), nums.end());
        int ans = -1;
        for (int num:nums){
            int sq = sqrt(num);
            if (sq*sq==num && d.find(sq)!=d.end()){
                d[num] = d[sq]+1;
                ans = max(ans, d[num]);
            }
            else{
                d[num] = 1;
            }
        }
        return ans;
    }
};