# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Convert into 21 merge two sorted lists
# Divide and conquer

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        step = 1
        while step < len(lists):
            for i in range(0, len(lists) - step, step * 2):  # skip 2*step for the next merge
                lists[i] = self.mergeTwoLists(lists[i], lists[i + step])  # step: the distance between two merged lists
            step *= 2

        return lists[0]

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = head = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next

        head.next = l1 if l1 else l2

        return dummy.next

