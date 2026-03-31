// Last updated: 3/31/2026, 9:40:48 PM
class Solution {
public:
    int trap(vector<int>& height) {
    int n = height.size();
    vector<int> lm(n), rm(n);
    lm[0] = height[0];
    for (int i = 1;i<n;i++){
        lm[i] = max(lm[i-1],height[i]);
    }
    rm[n-1] = height[n-1];
    for (int j =n-2;j>=0;j--){
        rm[j] = max(rm[j+1],height[j]);
    }

    int water = 0;
    for (int k = 0; k < n; k++) {
        water += min(lm[k], rm[k]) - height[k];
    }
    return water;
    }
};