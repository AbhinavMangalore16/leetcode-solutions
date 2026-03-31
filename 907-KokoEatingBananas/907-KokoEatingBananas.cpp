// Last updated: 3/31/2026, 9:36:32 PM
#include <vector>
#include <algorithm>

class Solution {
public:
    bool kokoEats(const std::vector<int>& piles, int k, int h) {
        int koko = 0;
        for (auto p : piles) {
            koko += (p+k-1) / k; 
        }
        return koko <= h;
    }

    int minEatingSpeed(std::vector<int>& piles, int h) {
        int low = 1;
        int high = *std::max_element(piles.begin(), piles.end());

        while (low < high) {
            int mid = low + (high - low) / 2; 

            if (kokoEats(piles, mid, h)) {
                high = mid;
            } else {
                low = mid + 1; 
            }
        }

        return low; 
    }
};
