"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Example 3:
Input: root = [5,2,7,1,3,4,8]
Output: false
Explanation: The root node's value is 5 but its right grandchild's value is 4. 
The rule of binary search should constrain every node's value in the binary tree, 
which is the left side of nodes should always be little than the right side.
"""

from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def printBSTStructure(self, root: TreeNode, indent="") -> None:
        if root is None:
            return None
        else:
            print(indent, root.val)

        # add a new indent
        indent += "  "

        self.printBSTStructure(root.left, indent + "L")
        self.printBSTStructure(root.right, indent + "R")

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # print out the structure of tree
        # self.printBSTStructure(root)

        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            # debug
            val = node.val
            # print('tree node:', val, 'lower:', lower, 'upper:', upper, end=" ")
            
            # if not valid
            if val <= lower or val >= upper:
                # print("invalid")
                return False
            # else:
                # print("valid")

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)