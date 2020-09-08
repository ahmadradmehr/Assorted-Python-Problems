"""
Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class RemoveNthFromEnd:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        num_nodes = 0
        t = head
        while t:
            num_nodes += 1
            t = t.next
        if n == num_nodes:
            return head.next
        t = head
        while num_nodes - n > 1:
            num_nodes -= 1
            t = t.next
        t.next = t.next.next
        return head
