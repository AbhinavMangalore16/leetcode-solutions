// Last updated: 3/31/2026, 9:41:07 PM
class Solution {
public:
bool isValid(string s){
    stack <char> stk;
    for(int i = 0;i<s.length();i++){
        char ch = s[i];
        if(ch=='(' || ch=='[' || ch=='{'){
            stk.push(ch);
        }
        else{
            if (stk.empty()){
                return false;
            }
            else if(ch==')' && stk.top()=='(' && !stk.empty()){
                stk.pop();
            }
            else if(ch==']' && stk.top()=='[' && !stk.empty()){
                stk.pop();
            }
            else if(ch=='}' && stk.top()=='{' && !stk.empty()){
                stk.pop();
            }
            else{
                return false;
            }
        }
    }
    return stk.empty();
}
};