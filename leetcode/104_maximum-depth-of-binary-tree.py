# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxDepth(root: TreeNode) -> int:
	if not root:
		return 0
	if not root.left and not root.right:
		return 1
	if not root.left:
		return 1 + maxDepth(root.right)
	if not root.right:
		return 1 + maxDepth(root.left)
	return 1 + max(maxDepth(root.left), maxDepth(root.right))

root = TreeNode(3)
a_1 = TreeNode(9)
a_2 = TreeNode(20)
b_1 = TreeNode(15)
b_2 = TreeNode(7)
root.left = a_1
root.right = a_2
a_2.left = b_1
a_2.right = b_2

print(maxDepth(root))
