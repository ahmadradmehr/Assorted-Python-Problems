"""
Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class AddTwoNumbers(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ll = l = ListNode()
        rem = 0
        while l1 or l2 or rem == 1:
            l.next = ListNode()
            l = l.next
            if l1 and l2:
                l.val = (l1.val + l2.val + rem) % 10
                rem = (l1.val + l2.val + rem) // 10
                l1 = l1.next
                l2 = l2.next
            elif l1:
                l.val = (l1.val + rem) % 10
                rem = (l1.val + rem) // 10
                l1 = l1.next
            elif l2:
                l.val = (l2.val + rem) % 10
                rem = (l2.val + rem) // 10
                l2 = l2.next
            else:
                l.val = rem
                rem = 0;
        return ll.next
