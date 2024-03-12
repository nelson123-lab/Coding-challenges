# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        maxValue = -float('inf')
        slow, fast = head, head

        # Finding middle value
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Reversing
        curr, prev = slow, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Checking for max sum each time.
        while prev:
            maxValue = max(maxValue, (head.val + prev.val))
            head = head.next
            prev = prev.next
        
        return maxValue

"""
- Here inorder to find the max twin sum. We are first identifying the middle element of the linked list using the slow and fast pointer method. 
- Then we need to reverse the half part of the linkedlist using the curr and prev method to reverse a linked list.
- We iterate through the head and prev linkedList each time and compares with a maxValue variable to check which sum is maximum each time.

Time Complexity O(n)
Space Complexity O(1) we are not using any extra space.
"""

