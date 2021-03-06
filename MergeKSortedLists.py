"""
Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class MergeKSortedLists:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        while None in lists:
            lists.remove(None)
        if not lists:
            return None
        ind = 0
        for i in range(len(lists)):
            if lists[i].val < lists[ind].val:
                ind = i
        head = ListNode(lists[ind].val)
        lists[ind] = lists[ind].next
        if not lists[ind]:
            lists.pop(ind)
        t = head
        while len(lists) > 0:
            ind = 0
            for i in range(len(lists)):
                if lists[i].val < lists[ind].val:
                    ind = i
            t.next = ListNode(lists[ind].val)
            lists[ind] = lists[ind].next
            if not lists[ind]:
                lists.pop(ind)
            t = t.next
        return head
