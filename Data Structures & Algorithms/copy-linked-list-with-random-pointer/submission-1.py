"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None


        l_dict = {}

        node = head
        while node:
            dummy = Node(node.val, node.next, node.random)
            l_dict[node] = dummy
            node = node.next
        

        for node in l_dict:
            if node.next:
                l_dict[node].next = l_dict[node.next]
            else:
                l_dict[node].next = None
            if node.random:
                l_dict[node].random = l_dict[node.random]
            else:
                l_dict[node].random = None
        
        return l_dict[head]
        