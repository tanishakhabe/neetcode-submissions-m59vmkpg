# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Find length of the list N
        dummy = head
        N = 1
        while dummy.next:
            dummy = dummy.next
            N += 1
        print(N)


        # Remove (N-n)th node from the beginning
        rem_num = (N - n) + 1
        if rem_num == 1: 
            return head.next 

        curr = head
        curr_num = 1
        while curr_num < rem_num - 1:
            curr = curr.next
            curr_num += 1
        print(curr_num)
        print(rem_num)

        # Delete the node
        prev = curr
        to_del = curr.next
        tmp = curr.next.next
        to_del.next = None
        prev.next = tmp
    
        return head




