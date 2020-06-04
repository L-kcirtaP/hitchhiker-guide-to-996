# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return root
        
        left = self.flatten(root.left)
        right = self.flatten(root.right)

        if left:
            left_most = left
            while left_most.right:
                left_most = left_most.right
            root.left = None
            root.right = left
            left_most.right = right
        else:
            root.right = right

        return root

s = Solution()
root = TreeNode(1)
a1 = TreeNode(2)
a2 = TreeNode(5)
b1 = TreeNode(3)
b2 = TreeNode(4)
b3 = TreeNode(6)
root.left = a1
root.right = a2
a1.left = b1
a1.right = b2
a2.right = b3

s = Solution()
root = s.flatten(root)

while root:
    print(root.val)
    root = root.right
