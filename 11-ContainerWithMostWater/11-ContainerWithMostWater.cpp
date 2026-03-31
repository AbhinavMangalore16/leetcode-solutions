// Last updated: 3/31/2026, 9:41:24 PM
#define faster \
ios::sync_with_stdio(false);\
cin.tie(nullptr);\
cout.tie(nullptr);
class Solution {
public:
    int maxArea(vector<int>& height) {
        faster
        int l = 0;
        int r = height.size()-1;
        int maxx = 0,curr=0;
        while(l<r){
            curr = min(height[l], height[r])*(r-l);
            maxx = max(curr, maxx);
            if (height[l]<height[r]){
                l++;
            }
            else{
                r--;
            }
        }
        return maxx;
    }
};