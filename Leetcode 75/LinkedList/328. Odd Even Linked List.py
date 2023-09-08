# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Checking if there is no head, only one value or only 2 values respectively, then we can simply return the head.
        if not head or not head.next or not head.next.next:
            return head

        # Initializing odd and even pointers
        oddP = head
        evenP = head.next
        even_head = evenP

        while evenP is not None and evenP.next is not None:
            oddP.next = evenP.next
            oddP = oddP.next

            evenP.next = oddP.next
            evenP = evenP.next

        # Attach even list to the tail of odd list
        oddP.next = even_head

        return head

"""
- Here the problem is to rearrange the linkedList in a way that all the values in the odd index should group together and all the even index should be grouped and come after the odd indices.
- [1,2,3,4,5] changes to [1,3,5,2,4] here 1, 3, 5 are in the odd index positions so they were grouped together similarly 2 and 4 in the even index positions, thus grouped together.
- The problem requires us to do the operation in O(1) space compelxity so we won't be able to use extra space to make 2 separate linkedList for odd and even and then combine together.
- The only thing works here is rearranging the LinkedList to obtain the desired results

Time Compelxity O(n)
Space Complexity O(1)

"""

