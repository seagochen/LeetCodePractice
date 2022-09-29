/**
You are given a string s. You can convert s to a palindrome by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

 

Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"


Example 2:

Input: s = "abcd"
Output: "dcbabcd"
*/

class Solution {

    func shortestPalindrome(_ s: String) -> String {
        // if string is empty, return empty string
        if s.count == 0 {
            return ""
        }

        // if string has only one character, return that character
        if s.count == 1 {
            return s
        }

        // reverse string
        let reversed = String(s.reversed())

        // if string is already a palindrome, return string
        if s == reversed {
            return s
        }

        // compare the string s with reversed string
        for i in 0..<s.count {
            if s.hasPrefix(reversed.suffix(s.count - i)) {
                return reversed.prefix(i) + s
            }
        }

        // return the concatenated string, if no match found
        return reversed + s
    }
}