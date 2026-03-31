// Last updated: 3/31/2026, 9:38:36 PM
class Solution {
public:
bool isAnagram(string s, string t) {
        if (s.length()!=t.length()){
            return false;
        }
        int len = s.length();
        map<char, int> map;
        for(int i=0;i<=len;i++){
            map[s[i]]++;
            map[t[i]]--;
        }
        for (auto i:map){
            if (i.second){
                return false;
            }
        }
        return true;
}
};