// Last updated: 3/31/2026, 9:39:54 PM
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        vector<int> premin;
        int minn = INT_MAX;
        for(auto el:prices){
            minn = min(minn,el);
            premin.push_back(minn);
        }
        int maxd = -1;
        vector<int>::iterator it;
        for(int j = 0;j<prices.size();j++){
            if(maxd<(prices[j]-premin[j])){
                maxd = (prices[j]-premin[j]);
            }
        }
        return maxd;
    }
};