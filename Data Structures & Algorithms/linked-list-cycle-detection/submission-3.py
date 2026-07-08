# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        visited = [head]
        node = head
        while node.next:
            node = node.next
            if node in visited:
                return True
            visited.append(node)

        return False

        