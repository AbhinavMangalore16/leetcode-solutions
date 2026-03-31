// Last updated: 3/31/2026, 9:38:58 PM
#define faster \
ios::sync_with_stdio(false);\
cout.tie(NULL);\
cin.tie(NULL);
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        faster;
        if (s.length() != t.length()){return false;};
        vector<int> hS(200, 0);
        vector<int> hT(200, 0);
        for(int i=0;i<s.length();i++){
            if (hS[s[i]] != hT[t[i]]){
                return false;
            }
            hS[s[i]] = i+1;
            hT[t[i]] = i+1;
        }
        return true;
    }
};