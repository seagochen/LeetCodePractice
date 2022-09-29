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
        result = ListNode(0)
        result_tail = result
        carry = 0
                
        while l1 or l2 or carry:            
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            carry, out = divmod(val1 + val2 + carry, 10)    
                      
            result_tail.next = ListNode(out)
            result_tail = result_tail.next                      
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
               
        return result.next

def convertNodeList(l):
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


def main():
    # generate linked list
    # l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    # output: [8,9,9,9,0,0,0,1]
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

    s = Solution()
    print(convertNodeList(s.addTwoNumbers(l1, l2)))

if __name__ == "__main__":
    main()