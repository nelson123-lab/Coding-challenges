# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        # Initializing the pointers
        slow = head
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return head

"""
Here the middle node is getting removed by the using the slow and fast technique. The fast pointer always moves twice the speed of the slow pointer.
- This makes the slow pointer reach the middle when the fast pointer reach the end of the linked list.
- slow.next = slow.next.next enables the removal of the middle node.

Time Complexity O(n)
- Only 1 iteration is happening through the list.
Space Compelxity O(1)
- No additional space is used here for the algorithm.
"""
