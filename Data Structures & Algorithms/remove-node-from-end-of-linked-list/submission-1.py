class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        dummy = ListNode(0, head)
        curr = dummy
        for i in range(length - n):
            curr = curr.next

        curr.next = curr.next.next
        return dummy.next