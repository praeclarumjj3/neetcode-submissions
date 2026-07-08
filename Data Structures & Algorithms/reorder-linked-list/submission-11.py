# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None or head.next.next is None:
            return
        
        nodes = []
        node = head
        
        while node:
            nodes.append(node)
            node = node.next
        
        len_n = len(nodes)

        node = head
        last = nodes.pop()
        
        while node is not None and node != last:
            tmp = node.next
            last.next = tmp
            node.next = last
            node = tmp
            if tmp == last:
                break
            last = nodes.pop()

        node.next = None
