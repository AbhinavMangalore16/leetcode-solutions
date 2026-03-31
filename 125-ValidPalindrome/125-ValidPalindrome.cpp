// Last updated: 3/31/2026, 9:39:50 PM
class Solution {
public:
bool isPalindrome(string s){
    int n = s.size();
    int l = 0, u = n-1;
    while (l<u){
        while(l<u && !isalnum(s[l])){
            l++;
        }
        while(l<u && !isalnum(s[u])){
            u--;
        }
        if (tolower(s[l]) != tolower(s[u])){
            return false;
        }
        l++;
        u--;
    }
    return true;
}
};