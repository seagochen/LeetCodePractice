/**
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
 */


#include <iostream>
#include <map>

using namespace std;

// define a map to store the length of the chain
map<long, long> chainLength;

// define a function to calculate the length of the chain
long getChainLength(long n) {
    if (n == 1) {
        return 1;
    }
    if (chainLength.find(n) != chainLength.end()) {
        return chainLength[n];
    }
    if (n % 2 == 0) {
        chainLength[n] = getChainLength(n / 2) + 1;
    } else {
        chainLength[n] = getChainLength(3 * n + 1) + 1;
    }
    return chainLength[n];
}

int main()
{
    long maxChainLength = 0;
    long maxChainLengthStart = 0;

    for (long i = 1; i < 1000000; i++) {
        long chainLength = getChainLength(i);
        if (chainLength > maxChainLength) {
            maxChainLength = chainLength;
            maxChainLengthStart = i;
        }
    }

    cout << maxChainLengthStart << endl;
    return 0;
}
