# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        import heapq
        min_heap = []
        
        for i, ll in enumerate(lists):
            if ll is not None:
                heapq.heappush(min_heap, (ll.val, i, ll))

        while min_heap:
            # pop smallest node
            val, i, smallest_node = heapq.heappop(min_heap)

            # attach it to res
            curr.next = smallest_node
            curr = curr.next

            # push its .next onto the heap if it exists
            if smallest_node.next:
                heapq.heappush(min_heap, (smallest_node.next.val, i, smallest_node.next))

        return dummy.next

            
         
        