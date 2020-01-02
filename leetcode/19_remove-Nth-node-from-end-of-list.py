# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        items = [p.val]

        while p.next != None:
            items.append(p.val)
            p = p.next

        pos = len(items) - n
        if len(items) == 1:
            return []

        if pos == 0:
            return head.next

        ptr = ListNode(0)
        ptr.next = head
        current = 0
        while current < pos and ptr.next != None:
            ptr = ptr.next
            current += 1
        if ptr.next != None:
            ptr.next = ptr.next.next

        return head
