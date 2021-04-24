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
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        sum_num = l1.val + l2.val
        digit = sum_num % 10
        carry = int(sum_num / 10)
        l3 = ListNode(digit)
        ans = l3

        p1 = l1.next
        p2 = l2.next

        while p1 or p2:
            sum = carry
            if p1:
                sum += p1.val
                p1 = p1.next
            if p2:
                sum += p2.val
                p2 = p2.next
            digit = sum % 10
            carry = int(sum / 10)
            new_n = ListNode(digit)
            l3.next = new_n
            l3 = l3.next

        if carry != 0:
            new_n = ListNode(carry)
            l3.next = new_n
            l3 = l3.next

        return ans
