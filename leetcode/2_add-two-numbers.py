#coding=utf-8
import sys 
#str = input()
#print(str)
print('Hello,World!')

class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None


def generateZeroList(length):
    # length > 0!
    head = p = ListNode(0)
    for _ in range(length-1):
        p.next = ListNode(0)
        p = p.next
    return head, p


def sumList(head_a, head_b):
    if not head_a or not head_b:
        return head_a if head_a else head_b
    
    length_a = length_b = 0
    p_a, p_b = head_a, head_b
    while p_a:
        p_a = p_a.next
        length_a += 1
    while p_b:
        p_b = p_b.next
        length_b += 1
        
    if length_a > length_b:
        new_head_b, p_b = generateZeroList(length_a-length_b)
        p_b.next = head_b
        head_b = new_head_b
    if length_b > length_a:
        new_head_a, p_a = generateZeroList(length_b-length_a)
        p_a.next = head_a
        head_a = new_head_a

    head, flag = sumListCore(head_a, head_b)
    
    if flag:
        ret = ListNode(1)
        ret.next = head
    else:
        ret = head

    return ret


def sumListCore(p_a, p_b):
    if not p_a or not p_b:
        return
    cur_flag = False
    next_node, flag = sumListCore(p_a.next, p_b.next)

    cur_val = p_a.val + p_b.val + int(flag)
    if cur_val >= 10:
        cur_val -= 10
        cur_flag = True
    cur_node = ListNode(cur_val)
    cur_node.next = next_node

    return cur_node, cur_flag
