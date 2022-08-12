/**
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.


Example 2:

Input: s = "cbbd"
Output: "bb"
*/

class Solution {

    func isPalindrome(_ s: [Character], _ i: Int, _ j: Int) -> Bool {
        var ii = i
        var jj = j

        while ii < jj {
            if s[ii] != s[jj] {
                return false
            }
            ii += 1
            jj -= 1
        }
        return true
    }

    func longestPalindrome(_ s: String) -> String {
        // convert string to array of characters
        let chars = Array(s)

        // if string is empty, return empty string
        if chars.count == 0 {
            return ""
        }

        // if string has only one character, return that character
        if chars.count == 1 {
            return s
        }

        // initialize variables
        var longest = String(chars[0])

        // search from first of string to last of string
        for i in 0..<chars.count {
            for j in (i..<chars.count).reversed() {
                // if chars[i] == chars[j], then check if substring is palindrome
                if chars[i] == chars[j] && j - i >= longest.count {
                    if isPalindrome(chars, i, j) {
                        longest = String(chars[i...j])
                        // print(longest)
                    }
                }

                if longest.count >= j - i {
                    break
                }
            }
        }

        return longest
    }
}

func test() {
    let test_string1 = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    let test_string2 = "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"

    let solution = Solution()
    print(solution.longestPalindrome(test_string1))
    print(solution.longestPalindrome(test_string2))
}

test()