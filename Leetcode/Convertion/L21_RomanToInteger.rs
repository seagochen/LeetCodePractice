/**
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.


Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.


Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
*/

fn roman_to_int(s: String) -> i32 {
    // reverse the array and convert the string to char array
    let mut chars: Vec<char> = s.chars().collect();

    // create a hashmap to store the roman numerals
    let mut roman_map = std::collections::HashMap::new();

    roman_map.insert('I', 1);
    roman_map.insert('V', 5);
    roman_map.insert('X', 10);
    roman_map.insert('L', 50);
    roman_map.insert('C', 100);
    roman_map.insert('D', 500);
    roman_map.insert('M', 1000);

    // create a variable to store the result
    let mut result = 0;
    let mut i = 0;

    // loop through the char array
    while i < chars.len() {
        // if the current char is I and the next char is V or X
        if chars[i] == 'I' && (i + 1 < chars.len()) && (chars[i + 1] == 'V' || chars[i + 1] == 'X') {
            // add the value of the next char to the result
            result += roman_map.get(&chars[i + 1]).unwrap();
            // subtract the value of the current char from the result
            result -= roman_map.get(&chars[i]).unwrap();
            // increment i by 2
            i += 2;
        // if the current char is X and the next char is L or C
        } else if chars[i] == 'X' && (i + 1 < chars.len()) && (chars[i + 1] == 'L' || chars[i + 1] == 'C') {
            // add the value of the next char to the result
            result += roman_map.get(&chars[i + 1]).unwrap();
            // subtract the value of the current char from the result
            result -= roman_map.get(&chars[i]).unwrap();
            // increment i by 2
            i += 2;
        // if the current char is C and the next char is D or M
        } else if chars[i] == 'C' && (i + 1 < chars.len()) && (chars[i + 1] == 'D' || chars[i + 1] == 'M') {
            // add the value of the next char to the result
            result += roman_map.get(&chars[i + 1]).unwrap();
            // subtract the value of the current char from the result
            result -= roman_map.get(&chars[i]).unwrap();
            // increment i by 2
            i += 2;
        // if the current char is not I, X or C
        } else {
            // add the value of the current char to the result
            result += roman_map.get(&chars[i]).unwrap();
            // increment i by 1
            i += 1;
        }
    }

    // return the result
    result
}


fn main (){
    println!("{}", roman_to_int("MCMXCIV".to_string())); // 1994
    println!("{}", roman_to_int("LVIII".to_string())); // 58
    println!("{}", roman_to_int("III".to_string())); // 3
    println!("{}", roman_to_int("DCXXI".to_string())); // 621
}