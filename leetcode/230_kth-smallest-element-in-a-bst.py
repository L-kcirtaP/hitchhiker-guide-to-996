# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.res = 0
        self.k = k
        def helper(root):
            if not root:
                return
            if root.left:
                helper(root.left)
            self.k -= 1
            if self.k == 0:
                self.res = root.val
                return
            if root.right:
                helper(root.right)

        helper(root)
        return self.res

root = TreeNode(3)
n1 = TreeNode(1)
n2 = TreeNode(4)
n3 = TreeNode(2)
root.left = n1
root.right = n2
n1.right = n3

s = Solution()
print(s.kthSmallest(root, 3))
