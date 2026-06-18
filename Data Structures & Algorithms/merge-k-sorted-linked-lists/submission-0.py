import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        counter = 0
        for head in lists:
            if head:
                counter +=2
                arr.append((head.val, counter, head))
        
        heapq.heapify(arr)
        dummy = ListNode(-1, -1)
        curr = dummy
        if not arr:
            return
            
        while True:
            val, counter, ptr = heapq.heappop(arr)
            curr.next = ptr
            curr = ptr

            next_node = ptr.next
            if next_node is None:
                if not arr:
                    break
                continue
            counter +=3
            heapq.heappush(arr, (next_node.val, counter, next_node))
        
        return dummy.next
            
        