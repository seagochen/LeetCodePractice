// The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
// 
// 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
// 
// Let us list the factors of the first seven triangle numbers:
// 
//  1: 1
//  3: 1,3
//  6: 1,2,3,6
// 10: 1,2,5,10
// 15: 1,3,5,15
// 21: 1,3,7,21
// 28: 1,2,4,7,14,28
// We can see that 28 is the first triangle number to have over five divisors.
// 
// What is the value of the first triangle number to have over five hundred divisors?

// import list
use std::collections::LinkedList;

// compute factors of a given number
fn factors(n: u64) -> LinkedList<u64> {
    let mut factors = LinkedList::new();
    let mut i = 1;
    while i * i <= n {
        if n % i == 0 {
            factors.push_back(i);
            if i * i != n {
                factors.push_back(n / i);
            }
        }
        i += 1;
    }
    factors
}


fn main() {
    let mut triangle = 0;
    let mut i = 1;
    loop {
        triangle += i;
        i += 1;
        let f = factors(triangle);
        if f.len() > 500 {
            println!("{}", triangle);
            break;
        }
    }
}