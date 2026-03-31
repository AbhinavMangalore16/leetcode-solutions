// Last updated: 3/31/2026, 9:38:22 PM
// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int ans = -1;
        int low = 1, high = n;
        while(low<=high){
            int mid = low+(high-low)/2;
            if (isBadVersion(mid)){
                high = mid-1;
                ans = mid;
            }
            else{
                low = mid+1;
            }
        }
        return ans;
    }
};