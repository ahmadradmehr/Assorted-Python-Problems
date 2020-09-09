"""
Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class SwapNodesInPairs:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        l = head
        ll = head.next
        l.next = head.next.next
        ll.next = l
        head = ll
        l, ll = ll, l
        while ll.next and ll.next.next:
            l = ll.next
            ll.next = l.next
            ll = ll.next
            l.next = ll.next
            ll.next = l
            l, ll = ll, l
        return head
