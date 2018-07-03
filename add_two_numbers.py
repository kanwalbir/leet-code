# https://leetcode.com/problems/add-two-numbers/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def array_to_linked_list(arr):

    ll = ListNode(arr[0])
    curr_node = ll

    for i in range(1, len(arr)):
        curr_node.next = ListNode(arr[i])
        curr_node = curr_node.next

    return ll


def linked_list_to_array(ll):
    
    arr = []
    curr_node = ll

    while curr_node:
        arr.append(curr_node.val)
        curr_node = curr_node.next

    return arr


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        carry = 0
        x = l1
        y = l2
        output_ll = None
        curr_node = None

        while (x or y):
            
            if (x and y):
                sub = x.val + y.val + carry
            elif x:
                sub = x.val + carry
            else:
                sub = y.val + carry

            if (sub > 9):
                carry = 1
                sub = sub - 10
            else:
                carry = 0

            if output_ll is None:
                curr_node = ListNode(sub)
                output_ll = curr_node
            else:
                curr_node.next = ListNode(sub)
                curr_node = curr_node.next
            
            if x:
                x = x.next
            if y:
                y = y.next
        
        if carry > 0:
            curr_node.next = ListNode(carry)
            
        return output_ll


ll1 = array_to_linked_list([1, 2, 3])
ll2 = array_to_linked_list([4, 5, 6])
ll3 = Solution().addTwoNumbers(ll1, ll2)  # 321 + 654 = 975 => [5, 7, 9]
print(linked_list_to_array(ll3))

ll1 = array_to_linked_list([2, 4, 3])
ll2 = array_to_linked_list([5, 6, 4])
ll3 = Solution().addTwoNumbers(ll1, ll2)  # 342 + 465 = 807 => [7, 0, 8]
print(linked_list_to_array(ll3))

ll1 = array_to_linked_list([2, 3])
ll2 = array_to_linked_list([0])
ll3 = Solution().addTwoNumbers(ll1, ll2)  # 32 + 0 = 32 => [2, 3]
print(linked_list_to_array(ll3))

ll1 = array_to_linked_list([9])
ll2 = array_to_linked_list([9])
ll3 = Solution().addTwoNumbers(ll1, ll2)  # 9 + 9 = 18 => [8, 1]
print(linked_list_to_array(ll3))
