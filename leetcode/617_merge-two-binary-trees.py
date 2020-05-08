# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return
        if not t1:
            return t2
        if not t2:
            return t1
        new_root = TreeNode(t1.val+t2.val)
        new_root.left = self.mergeTrees(t1.left, t2.left)
        new_root.right = self.mergeTrees(t1.right, t2.right)
        return new_root


t1 = TreeNode(1)
a1 = TreeNode(3)
a2 = TreeNode(2)
a3 = TreeNode(5)
t1.left = a1
t1.right = a2
a1.left = a3
t2 = TreeNode(2)
b1 = TreeNode(1)
b2 = TreeNode(3)
b3 = TreeNode(4)
b4 = TreeNode(7)
t2.left = b1
t2.right = b2
b1.right = b3
b2.right = b4

s = Solution()
root = s.mergeTrees(t1, t2)
