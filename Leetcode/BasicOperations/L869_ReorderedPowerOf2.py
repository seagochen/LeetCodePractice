"""
You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.

 

Example 1:

Input: n = 1
Output: true
Example 2:

Input: n = 10
Output: false

Constraints:

1 <= n <= 109
"""

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:

        """
        numbers: 1 2 4 8 16 32 64 128 256 512 1024 2048 4096 8192
        length:  1 1 1 1  2  2  2   3   3   3    4    4    4    4 
        power:   0 1 2 3  4  5  6   7   8   9   10   11   12   13
        """

        length = len(str(n))
        c = sorted(str(n))

        for i in range((length-1) * 3 + length // 3, length * 3 + length // 3 + 1):
            # number in 1 to 10, its available boundary is in 1 to 2
            # number in 10 to 100, its available boundary is in  2 to 3
            # so we can use i // 3 to get the available boundary

            if c == sorted(str(1 << i)):
                # if c is 256, sorted will be [2 ,5, 6]
                # 1 << i will be 256, and its sorted list will also be [2, 5, 6]
                # then return True
                return True
                
        return False


if __name__ == "__main__":
    test = Solution()
    print(test.reorderedPowerOf2(10))