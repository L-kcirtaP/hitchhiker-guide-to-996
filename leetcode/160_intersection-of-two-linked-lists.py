# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    p_a = headA
    len_a = 0
    while p_a:
        len_a += 1
        p_a = p_a.next

    p_b = headB
    len_b = 0
    while p_b:
        len_b += 1
        p_b = p_b.next

    p_a = headA
    p_b = headB
    ret = None
    if len_a > len_b:
        for _ in range(len_a-len_b):
            p_a = p_a.next
    else:
        for _ in range(len_b-len_a):
            p_b = p_b.next

    while p_a:
        if p_a == p_b:
            if not ret:
                ret = p_a
        else:
            ret = None
        p_a = p_a.next
        p_b = p_b.next

    return ret
