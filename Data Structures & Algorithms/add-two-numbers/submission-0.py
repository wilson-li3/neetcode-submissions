# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        curr = head
        carry = 0
        while l1 or l2 or carry == 1:

            nex = ListNode()
            curr.next = nex
            curr = nex

            if l1:
                curr.val += l1.val
            
            if l2:
                curr.val += l2.val

            curr.val += carry

            if curr.val >= 10:
                curr.val %= 10
                carry = 1
            else:
                carry = 0

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return head.next


        