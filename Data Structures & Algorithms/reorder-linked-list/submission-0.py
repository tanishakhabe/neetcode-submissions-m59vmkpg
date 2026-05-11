# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle point of the linked list.
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next # start of the second half of the list

        # reverse the second half of the list
        slow.next = None
        prev = None
        
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        # merge the two halves of the list
        first = head
        second = prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2





    
        


        
        