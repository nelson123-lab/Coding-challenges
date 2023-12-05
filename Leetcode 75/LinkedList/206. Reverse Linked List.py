# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
        return prev

"""
The reverseList method initializes prev to None and curr to the head of the linked list. 
Then, it iterates through the linked list, reversing the pointers to the nodes. Finally, it returns the new head of the reversed linked list.
"""
