#include <string>
#include <iostream>
#include <math.h>
#include <limits.h>

using namespace std;

class Solution {
public:
    int myAtoi(string str) {
        if (str.empty()) {
            return 0;
        }

        int start = 0;
        int end = str.length()-1;
        bool negative = false;
        bool valid;

        for (int i = 0; i < str.length(); i++) {

            if (valid && str[i] == ' ') {               // reach the end of integral number
                valid = false;
                end = i-1;
                break;
            };

            if (str[i] == '-') {
                negative = true;
            } else if (str[i] >= '0' && str[i] <= '9') {  // is digit
                if (!valid) {
                    valid = true;
                    start = i;
                };
            } else if (str[i] == ' ') {
                continue;
            } else {
                return 0;
            }
        }

        unsigned res = 0;
        int digit = end-start;
        if (!valid && end == str.length()-1) {
            return 0;
        } else {
            for (int i = start; i <= end; i++) {
                unsigned tmp = res;
                tmp += static_cast<int>(str[i]-'0') * pow(10, digit--);
                if (tmp < res) {
                    return negative ? INT_MIN : INT_MAX;
                }
                res = tmp;
            }
        }

        return negative ? -res : res;
    }
};

int main() {
    Solution s = Solution();
    cout << s.myAtoi("") << endl;
    cout << s.myAtoi("123") << endl;
    cout << s.myAtoi(" 123 ") << endl;
    cout << s.myAtoi("   -42") << endl;
    cout << s.myAtoi("4193 with words") << endl;
    cout << s.myAtoi("words and 987") << endl;
    cout << s.myAtoi("  words and   -987 ") << endl;
    cout << s.myAtoi("-91283472332") << endl;
}