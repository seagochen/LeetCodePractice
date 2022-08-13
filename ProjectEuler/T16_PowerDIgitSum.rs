/**
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
*/

fn string_pow(base: i32, power: i32) -> String {
    // convert the base to string
    let mut base_str = base.to_string();

    // multiply the base by itself power times
    for _ in 1..power {
        let mut carry = 0;
        let mut result = String::new();

        // multiply each digit of the base by the base
        for digit in base_str.chars().rev() {
            let digit = digit.to_digit(10).unwrap();
            let product = digit * base as u32 + carry;
            carry = product / 10;
            result.push_str(&(product % 10).to_string());
        }

        // add the carry to the result
        if carry > 0 {
            result.push_str(&carry.to_string());
        }

        // reverse the result and set it as the new base
        base_str = result.chars().rev().collect();
    }

    base_str
}

fn main() {
    let mut num = string_pow(2, 1000);
    let sum = num.chars().map(|c| c.to_digit(10).unwrap()).sum::<u32>();
    println!("{}", sum);
}