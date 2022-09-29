"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        # define a new linked list
        l1_back = self.convertNodeList(l1)
        l2_back = self.convertNodeList(l2)

        # add the two numbers
        l3_back = l1_back + l2_back

        # convert l3 to linked list
        return self.convertIntToNodeList(l3_back)
        
    def convertNodeList(self, l):
        l_copy = []

        # convert listnode to list
        node = l
        while True:
            l_copy.append(node.val)
            
            if node.next == None:
                break
            else:
                node = node.next

        # convert the list to int
        l_copy.reverse()
        l_int = int(''.join(map(str, l_copy)))
        return l_int

    def convertIntToNodeList(self, l):
        l_str = str(l)
        l_list = list(l_str)
        l_list.reverse()
        
        # convert the list to listnode
        l_node = ListNode()
        next_node = l_node
        
        for i in range(len(l_list)):
            next_node.val = int(l_list[i])

            if i != len(l_list) - 1:
                next_node.next = ListNode()
                next_node = next_node.next

        print(self.convertNodeList(l_node))
                
        return l_node
        
def main():
    # generate linked list
    # l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    # output: [8,9,9,9,0,0,0,1]
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

    s = Solution()
    s.addTwoNumbers(l1, l2)

if __name__ == "__main__":
    main()