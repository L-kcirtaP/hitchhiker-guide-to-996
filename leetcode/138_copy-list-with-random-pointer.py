
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head: 'Node') -> 'Node':
    if not head:
        return

    tmp = head
    while tmp:
        nxt = tmp.next
        tmp.next = Node(tmp.val)
        tmp.next.next = nxt
        tmp = tmp.next.next

    tmp = head
    while tmp:
        if tmp.random:
            tmp.next.random = tmp.random.next
        tmp = tmp.next.next

    tmp = head.next
    while tmp.next:
        tmp.next = tmp.next.next
        tmp = tmp.next

    return head.next
