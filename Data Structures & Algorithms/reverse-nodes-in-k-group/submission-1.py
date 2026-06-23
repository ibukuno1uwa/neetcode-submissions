# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, -1)

        prevGroup = dummy
        curr = head
        old_head = head
        prev = dummy

        tcurr = head
        n = 0
        while tcurr:
            n +=1
            tcurr = tcurr.next

        c = 0
        while curr:
            c +=1

            curr_next = curr.next
            curr.next = prev
            prev = curr

            curr = curr_next
            
            if c % k == 0:
                prevGroup.next = prev
                prevGroup = old_head
                
                if n - c < k:
                    old_head.next = curr
                    return dummy.next
                old_head = curr

        return dummy.next