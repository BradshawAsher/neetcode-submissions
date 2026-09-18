# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #1. find the middle and then use a slow and fast pointer to split the list into two halves
        #2. Reverse the second half: invert the .next pointers of the back half in place
        #3. Merge alternating nodes: interleave nodes from the first and second lists
        if not head or not head.next:
            return

        #1. Find the middle of the list (slow will point to the end of the first half)
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #split the two lists
        second = slow.next
        slow.next = None

        #2. Reverse the second half
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        second = prev #prev is now the head of the reversed half

        #3. Interleave first and second halves
        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2



        