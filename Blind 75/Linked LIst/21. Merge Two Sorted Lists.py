# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        ll = sorted_list = Node()

        while l1 and l2:
            if l1.val <= l2.val:
                sorted_list.next = l1
                l1 = l1.next
                sorted_list = sorted_list.next
            else:
                sorted_list.next = l2
                l2 = l2.next
                sorted_list = sorted_list.next
        if l1:
            sorted_list.next = l1
        if l2:
            sorted_list.next = l2
        return ll.next
