# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: ListNode) -> bool:
    if not head:
        return False
    fast = slow = head
    while fast and fast.next:
        fast = fast.next
        if fast == slow:
            return True
        fast = fast.next
        slow = slow.next

    return False

a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
d.next = b
print(hasCycle(a))