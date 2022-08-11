"""
Example 1:
Input: nums = [1,2,3,4,3]
Output: [3, 5]

Example 2:
Input: nums = [1,2,2]
Output: [2, 3]
"""

def findErrorNums(nums):
    # Find the duplicate number
    for i in range(len(nums)):
        if nums[i] in nums[i + 1:]:
            duplicate = nums[i]
            break
    # Find the missing number
    for i in range(1, len(nums) + 1):
        if i not in nums:
            missing = i
            break
    return [duplicate, missing]

def main():
    nums = [1, 2, 2]
    print(findErrorNums(nums))

if __name__ == "__main__":
    main()