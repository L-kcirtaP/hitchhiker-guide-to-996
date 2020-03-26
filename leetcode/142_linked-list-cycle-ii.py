class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head: ListNode) -> ListNode:
    if not head:
        return None

    fast = slow = head
    while fast and fast.next:
        fast = fast.next
        if fast == slow:
            break
        fast = fast.next
        slow = slow.next

    if fast and fast.next:
    	fast = fast.next
    	slow = head
    	while fast != slow:
    		fast = fast.next
    		slow = slow.next
    	return slow

    return None

a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
d.next = b

ret = detectCycle(a)
