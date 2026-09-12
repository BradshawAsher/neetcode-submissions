# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #make a new list
        prev = None
        curr = head

        while curr:
            next_temp = curr.next #1. Save the next node
            curr.next = prev #2. Reverse the pointer
            prev = curr #3. Move prev forward
            curr = next_temp #4. Move curr forward
        
        return prev

        