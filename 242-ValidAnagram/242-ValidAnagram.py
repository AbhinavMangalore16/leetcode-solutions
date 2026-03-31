# Last updated: 3/31/2026, 9:38:31 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        diction = {}
        for i in range(len(s)):
            diction[s[i]]=diction.get(s[i],0)+1
            diction[t[i]]=diction.get(t[i],0)-1
        for i in diction.values():
            if i!=0:
                return False
        return True
#        class Solution {
# public:
# bool isAnagram(string s, string t) {
#         if (s.length()!=t.length()){
#             return false;
#         }
#         int len = s.length();
#         map<char, int> map;
#         for(int i=0;i<=len;i++){
#             map[s[i]]++;
#             map[t[i]]--;
#         }
#         for (auto i:map){
#             if (i.second){
#                 return false;
#             }
#         }
#         return true;
# }
# };