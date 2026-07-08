# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head.next is None:
            return None
        
        len_n = 0
        node = head

        while node:
            len_n += 1
            node = node.next

        remove_index = len_n - n


        prev = None
        cur = head
        count = 0
        while cur:
            if count == remove_index:
                if prev is None:
                    head = cur.next
                    return head
                else:
                    prev.next = cur.next
                    cur.next = None
                    return head
            prev = cur
            cur = cur.next
            count += 1


