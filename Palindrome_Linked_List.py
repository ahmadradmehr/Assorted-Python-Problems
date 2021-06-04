"""
*** Palindrome Linked List ***


Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head.next
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow1 = head
        slow2 = self.reverse(slow)
        while slow2:
            if slow1.val != slow2.val:
                return False
            slow1 = slow1.next
            slow2 = slow2.next
        return True

    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        nex = head
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        return prev

