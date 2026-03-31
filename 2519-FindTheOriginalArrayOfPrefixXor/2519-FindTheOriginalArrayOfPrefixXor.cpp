// Last updated: 3/31/2026, 9:31:31 PM
class Solution {
public:
    vector<int> findArray(vector<int>& pref) {
        int i;
        vector<int> orgArray(pref.size());
        orgArray[0] = pref[0];
        for(i=1;i<pref.size();i++){
            orgArray[i] = pref[i-1] ^ pref[i];
        }
        return orgArray;
    }
};