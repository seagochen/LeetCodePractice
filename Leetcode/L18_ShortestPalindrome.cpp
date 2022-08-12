#include <string>

using namespace std;


class Solution {
public:
    string shortestPalindrome(string s) {

        // compare the string with its reverse
        int n = s.size();
        int i = 0;
        for (int j = n - 1; j >= 0; j--) {
            if (s[i] == s[j])
                i++;
        }
        if (i == n) {
            return s;
        }

        // reverse the suffix and add it to the front
        string remain_rev = s.substr(i, n);
        reverse(remain_rev.begin(), remain_rev.end());

        return remain_rev + shortestPalindrome(s.substr(0, i)) + s.substr(i);
    }
};