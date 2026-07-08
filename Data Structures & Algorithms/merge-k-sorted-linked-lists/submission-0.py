class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge(l1, l2):
            dummy = ListNode(0)
            cur = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next

            cur.next = l1 if l1 else l2
            return dummy.next

        def divide(left, right):
            if left > right:
                return None
            if left == right:
                return lists[left]

            mid = (left + right) // 2
            l1 = divide(left, mid)
            l2 = divide(mid + 1, right)

            return merge(l1, l2)

        return divide(0, len(lists) - 1)