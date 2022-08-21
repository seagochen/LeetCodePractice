"""
You are given two strings stamp and target. Initially, there is a string s of length target.length with all s[i] == '?'.

In one turn, you can place stamp over s and replace every letter in the s with the corresponding letter from stamp.

For example, if stamp = "abc" and target = "abcba", then s is "?????" initially. In one turn you can:
place stamp at index 0 of s to obtain "abc??",
place stamp at index 1 of s to obtain "?abc?", or
place stamp at index 2 of s to obtain "??abc".
Note that stamp must be fully contained in the boundaries of s in order to stamp (i.e., you cannot place stamp at index 3 of s).
We want to convert s to target using at most 10 * target.length turns.

Return an array of the index of the left-most letter being stamped at each turn. If we cannot obtain target from s within 10 * target.length turns, return an empty array.


Example 1:

Input: stamp = "abc", target = "ababc"
Output: [0,2]
Explanation: Initially s = "?????".
- Place stamp at index 0 to get "abc??".
- Place stamp at index 2 to get "ababc".
[1,0,2] would also be accepted as an answer, as well as some other answers.


Example 2:

Input: stamp = "abca", target = "aabcaca"
Output: [3,0,1]
Explanation: Initially s = "???????".
- Place stamp at index 3 to get "???abca".
- Place stamp at index 0 to get "abcabca".
- Place stamp at index 1 to get "aabcaca".
"""

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        tmp = target
        log = []
        for _ in range(10 * len(target)):
            f = self.find(stamp, tmp)
            if f == -1:
                return []
            else:
                tmp = tmp[:f] + "?" * len(stamp) + tmp[f + len(stamp):]
                log.append(f)
            if tmp == "?" * len(target):
                return log[::-1]
        return log[::-1] if tmp == "?" * len(target) else [] 
        
    def find(self, s1, s2):
        for i in range(len(s2) - len(s1) + 1):
            f = True
            if s2[i:i+len(s1)] == "?" * len(s1):
                continue
            for j in range(i, i + len(s1)):
                if s2[j] != s1[j - i] and s2[j] != "?":
                    f = False
                    break
            if f:
                return i
        return -1