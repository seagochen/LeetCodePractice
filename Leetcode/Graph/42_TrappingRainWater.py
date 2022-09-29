"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

                                                                               
%                                                                           
,                                                                           
,                                                                           
*                                           @@@@@@@                         
,                                           @@@@@@@                         
,                                           @@@@@@@                         
,                  @@@@@@@((((((((((((((((((@@@@@@@@@@@@@#(((((@@@@@@@      
,                  @@@@@@@((((((((((((((((((@@@@@@@@@@@@@#(((((@@@@@@@      
*      @@@@@@((((((@@@@@@@@@@@@@((((((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
,      @@@@@@((((((@@@@@@@@@@@@@((((((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
,      @@@@@@((((((@@@@@@@@@@@@@((((((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                                                
Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.


Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""

from typing import List


class Solution:

    # def left_max(self, height, i):
    #     max = 0
    #     for j in range(i):
    #         if height[j] > max:
    #             max = height[j]
    #     return max

    # def right_max(self, height, i):
    #     max = 0
    #     for j in range(i+1, len(height)):
    #         if height[j] > max:
    #             max = height[j]
    #     return max

    # def trap(self, height: List[int]) -> int:

    #     # left_sides and right_sides
    #     left_sides = [0] * len(height)
    #     right_sides = [0] * len(height)

    #     # given the height of each bar, compute how much water it can trap after raining
    #     for i in range(len(height)):
    #         left_sides.append(self.left_max(height, i))
    #         right_sides.append(self.right_max(height, i))

    #     # compute the water
    #     water = 0
    #     for i in range(len(height)):
    #         remain = min(left_sides[i], right_sides[i]) - height[i]
    #         if remain > 0:
    #             water += remain
        
    #     return water

    def trap(self, height: List[int]) -> int:
        # maximum height of left and right sides of each bar
        left_max = [0] * len(height)
        right_max = [0] * len(height)

        max_left_val = 0
        max_right_val = 0

        # compute the maximum height of left and right side of each bar
        for i in range(1, len(height)):
            # compare the left side of left max
            left_max[i] = max(max_left_val, height[i - 1])
            max_left_val = left_max[i]
        
        # compute the maximum height of right side of each bar
        for i in range(len(height) - 2, -1, -1):
            # compare the right side of right max
            right_max[i] = max(height[i + 1], max_right_val)
            max_right_val = right_max[i]

        # print(left_max, right_max)

        # compute the water
        water = 0
        for i in range(len(height)):
            remain = min(left_max[i], right_max[i]) - height[i]
            if remain > 0:
                water += remain
        
        return water
     

def test():
    s = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(s.trap(height))

    height = [4,2,0,3,2,5]
    print(s.trap(height))

if __name__ == "__main__":
    test()
    print("Done")