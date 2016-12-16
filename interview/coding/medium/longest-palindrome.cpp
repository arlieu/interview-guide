/*Find the longest palindromic substring in a given string.*/


#include <iostream>
#include <string>
using namespace std;


string substring(string s, int left, int right);


string longestPalindrome(string s) {
    if (s.length() == 0 || s.length() == 1) {
        return s;
    }

    string max = "";
    for (int i=0; i<s.length()-1; i++) {
        string odd = substring(s, i, i);
        if (odd.length() > max.length()) {
            max = odd;
        }

        string even = substring(s, i, i+1);
        if (even.length() > max.length()) {
            max = even;
        }
    }

    if (max == "") {
        max = s[0];
    }

    return max;
}


string substring(string s, int left, int right) {
    while (left >= 0 && right < s.length() && s[left] == s[right]) {
        left--;
        right++;
    }

    return s.substr(left+1, right-left-1);
}