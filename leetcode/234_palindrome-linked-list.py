# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True

        p = head
        n = 0
        while p:
            p = p.next
            n += 1
        p = head
        for _ in range(n//2):
            p = p.next
        tail = self.reverseList(p)

        res = True
        for _ in range(n//2):
            res &= head.val == tail.val
            head = head.next
            tail = tail.next
        return res


s = Solution()
s.isPalindrome(None)
