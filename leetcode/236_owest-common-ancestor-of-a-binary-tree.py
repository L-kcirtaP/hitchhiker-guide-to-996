# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def hasNode(self, root: 'TreeNode', node: 'TreeNode'):
        if not root:
            return False
        if root == node:
            return True
        return self.hasNode(root.left, node) or self.hasNode(root.right, node)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        pInLeft = self.hasNode(root.left, p)
        pInRight = self.hasNode(root.right, p)
        qInLeft = self.hasNode(root.left, q)
        qInRight = self.hasNode(root.right, q)

        if p == root or q == root:
            return root
        if (pInLeft and qInRight)\
            or (qInLeft and pInRight):
            return root
        if pInLeft and qInLeft:
            return self.lowestCommonAncestor(root.left, p, q)
        if pInRight and qInRight:
            return self.lowestCommonAncestor(root.right, p, q)


root = TreeNode(3)
a1 = TreeNode(5)
a2 = TreeNode(1)
b1 = TreeNode(6)
b2 = TreeNode(2)
b3 = TreeNode(0)
b4 = TreeNode(8)
c1 = TreeNode(7)
c2 = TreeNode(4)
root.left = a1
root.right = a2
a1.left = b1
a1.right = b2
a2.left = b3
a2.right = b4
b2.left = c1
b2.right = c2

s = Solution()
ret = s.lowestCommonAncestor(root, a1, c2)
print(ret.val)
