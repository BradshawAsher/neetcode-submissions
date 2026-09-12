# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #make a new list
        fake_head = ListNode(-1)
        temp_head = fake_head

        #go all the way through the current head/list until the last element, then work your way back???

        #stupid way first, copy to a list, then go through it
        list_order = []

        while head:
            list_order.append(head.val)
            head = head.next

        #now we have the list order, now work on list_order
        for i in range(len(list_order)-1, -1, -1):
            cur = list_order[i]
            new_node = ListNode(cur)
            temp_head.next = new_node
            temp_head = temp_head.next

        return fake_head.next

        