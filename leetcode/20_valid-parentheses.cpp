class Solution {
public:
    bool isValid(string s) {
        if (s.empty()) {return true;}
        stack<char> stk;
        for (auto iter = s.begin(); iter != s.end(); iter++) {
            char bar = *iter;
            if (bar == '(' || bar == '[' || bar == '{') {
                stk.push(bar);
            }
            else {
                if (stk.empty()) {return false;}
                char foo = stk.top();
                switch (bar)
                {
                case ')':
                    if (foo != '(') {return false;}
                    break;
                case ']':
                    if (foo != '[') {return false;}
                    break;
                case '}':
                    if (foo != '{') {return false;}
                    break;
                default:
                    return false;
                }
                stk.pop();
            }
        }
        if (stk.empty()) {
            return true;
        } else {
            return false;
        }
    }
};
