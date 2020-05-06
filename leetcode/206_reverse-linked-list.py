# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head

        p = new_head = self.reverseList(head.next)
        while p.next:
            p = p.next
        p.next = head
        head.next = None

        return new_head


s = Solution()
head = ListNode(1)
n1 = ListNode(2)
n2 = ListNode(3)
n3 = ListNode(4)
head.next = n1
n1.next = n2
n2.next = n3
head = s.reverseList(head)

p = head
while p:
    print(p.val)
    p = p.next
