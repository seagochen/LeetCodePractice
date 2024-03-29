/**
You are given an integer array nums that is sorted in non-decreasing order.

Determine if it is possible to split nums into one or more subsequences such that both of the following conditions are true:

Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more than the previous integer).
All subsequences have a length of 3 or more.
Return true if you can split nums according to the above conditions, or false otherwise.

A subsequence of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. (i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).

Example 1:

Input: nums = [1,2,3,3,4,5]
Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,5] --> 1, 2, 3
[1,2,3,3,4,5] --> 3, 4, 5


Example 2:

Input: nums = [1,2,3,3,4,4,5,5]
Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
[1,2,3,3,4,4,5,5] --> 3, 4, 5


Example 3:

Input: nums = [1,2,3,4,4,5]
Output: false
Explanation: It is impossible to split nums into consecutive increasing subsequences of length 3 or more.
*/

class Solution {
    func isPossible(_ nums: [Int]) -> Bool {
        
        var dict = [Int: Int]()
        for num in nums {
            dict[num, default: 0] += 1
        }
        
        var tails = [Int: Int]()
        
        for num in nums {
            if dict[num] == 0 {
                continue
            }
            
            if let tail = tails[num - 1], tail > 0 {
                tails[num - 1] = tail - 1
                tails[num, default: 0] += 1
            } else if let count = dict[num + 1], count > 0, let count2 = dict[num + 2], count2 > 0 {
                dict[num + 1] = count - 1
                dict[num + 2] = count2 - 1
                tails[num + 2, default: 0] += 1
            } else {
                return false
            }
            
            dict[num] = dict[num]! - 1
        }
        
        return true

    }
}

func test() {
    let s = Solution()
    assert(s.isPossible([1,2,3,3,4,5]) == true)
    assert(s.isPossible([1,2,3,3,4,4,5,5]) == true)
    assert(s.isPossible([1,2,3,4,4,5]) == false)
}

test()