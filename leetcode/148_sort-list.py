# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        tail = head
        while tail.next:
            tail = tail.next

        self.sortListCore(head, tail)
        return head

    def sortListCore(self, start, end):
        if start == end:
            return

        p1 = p2 = start.next
        p1_prev = start
        while p2 != end.next:
            if p2.val <= start.val:
                p1.val, p2.val = p2.val, p1.val
                if p1 != end:
                    p1 = p1.next
                    p1_prev = p1_prev.next
            p2 = p2.next

        if p1 == end:
            if p1.val < start.val:
                p1.val, start.val = start.val, p1.val

        self.sortListCore(start, p1_prev)
        self.sortListCore(p1, end)


head = ListNode(4)
n1 = ListNode(2)
n2 = ListNode(1)
n3 = ListNode(3)
n4 = ListNode(0)
head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
solution = Solution()
ini = solution.sortList(head)
print(ini.val)
print(ini.next.val)
print(ini.next.next.val)
print(ini.next.next.next.val)
print(ini.next.next.next.next.val)