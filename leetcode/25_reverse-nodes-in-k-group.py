# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverseList(head, end) -> ListNode:    
            if head == end or head.next == end:
                return head            
            new_head = reverseList(head.next, end)
            head.next.next = head
            head.next = None
            return new_head

        kth = head
        count = 0
        while kth and count < k:
            kth = kth.next
            count += 1

        new_head_1 = reverseList(head, kth)
        new_head_2 = self.reverseKGroup(kth, k)
        head.next = new_head_2
        return new_head_1


"""
面试时候写的现场代码

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverseList(head, tail):
    if head.next == tail:
        return head
    new_head = reverseList(head.next)
    head.next.next = head
    head.next = None
    return new_head

def reverseListByK(head, k):
    if not head.next:
        return

    count = 0
    k_forward = head
    while k_forward.next and count < k:
        k_forward = k_forward.next
        count += 1

    head.next.next = head
    head.next = reverseListByK(k_forward, k)
    new_head = reverseList(head, k_forward)
    return new_head
"""