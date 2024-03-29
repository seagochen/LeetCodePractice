/*
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.


Example 1:

Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.


Example 2:

Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.


Example 3:

Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.
*/

import Foundation

class Solution {

    func preprocess(_ s: String) -> String {
        // if s is empty, return 0
        if s.isEmpty {
            return "0"
        }

        // remove leading whitespace
        var s = s.trimmingCharacters(in: .whitespaces)

        // use regular expression to pick up the valid substring
        let regex = try! NSRegularExpression(pattern: "^[+-]?(\\d+)?\\.?(\\d+)")
        let match = regex.firstMatch(in: s, options: [], range: NSRange(location: 0, length: s.count))
        if let match = match {
            let range = match.range(at: 0)
            s = (s as NSString).substring(with: range)
        } else {
            return "0"
        }

        // reverse the string
        return String(s.reversed())
    }

    func postprocess(_ number: Double) -> Int {
        // if number is out of range, return the closest number
        if number > Double(Int32.max) {
            return Int(Int32.max)
        } else if number < Double(Int32.min) {
            return Int(Int32.min)
        } else {
            return Int(number)
        }
    }

    func myAtoi(_ s: String) -> Int {

        // process the string
        let s = preprocess(s)

        // use a decimal number to store the result
        var number = 0.0

        // carry bit
        var carry = 1.0

        // sign
        var sign = 1.0

        // float point
        var floatPoint = false

        // load the character from first to last
        for char in s {
            // if the character is not a number, skip it
            if !char.isNumber {

                // if the character is a sign, set the sign
                if char == "-" {
                    sign = -1.0
                }

                // if the character is a float point, set the float point
                if char == "." {
                    floatPoint = true

                    // if the float point is set, number should be decimal 
                    // so we should divide the number by carry
                    number /= carry

                    // reset the carry
                    carry = 1.0
                }

                continue
            }

            // if the character is a number, add it to the result
            number = number + Double(String(char))! * carry

            // update the carry bit
            carry = carry * 10.0
        }

        // if the float point is not set, number should be integer
        if !floatPoint {
            return postprocess(number * sign)
        } else {
            return Int(number * sign)
        }
    }
}