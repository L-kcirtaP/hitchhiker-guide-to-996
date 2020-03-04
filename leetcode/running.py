class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def rotateRight(head, k):
    if not (head and head.next):
        return head
    
    ptr = ListNode(head.val)
    ptr.next = head.next
    cnt = 1
    while ptr.next:
        cnt += 1
        ptr = ptr.next
    k = k % cnt
    if k == 0:
        return head

    ptr_s, ptr_f = ListNode(head.val), ListNode(head.val)
    ptr_s.next = head
    ptr_f.next = head
    for _ in range(k):
        ptr_f.next = ptr_f.next.next

    while ptr_f.next.next != None:
        ptr_s.next = ptr_s.next.next
        ptr_f.next = ptr_f.next.next
    new_head = ptr_s.next.next
    ptr_s.next.next = None
    ptr_f.next.next = head

    return new_head

x = ListNode(1)
y = ListNode(2)
x.next = y
# for i in range(1, 10):
#     x.next = ListNode(i)
#     x = x.next

head = rotateRight(x, 1)
