# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #can keep 2 pointers and just go
        #make a new list
        temp_head = ListNode(0)
        cur = temp_head

        #empty out 1 list, then attach the last node of list2 to the end, auto attached the rest of list 2

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
                cur = cur.next
            else:
                cur.next = list2
                list2 = list2.next
                cur = cur.next

        #list1 or list2 is empty
        if list1:
            cur.next = list1
        else:
            cur.next = list2
        
        return temp_head.next