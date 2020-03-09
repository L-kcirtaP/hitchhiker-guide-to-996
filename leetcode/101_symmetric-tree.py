# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSymmetric(root: TreeNode) -> bool:
    return twoTreesSymmetric(root.left, root.right)

def twoTreesSymmetric(root_1: TreeNode, root_2: TreeNode) -> bool:
	if not (root_1 or root_2):
		return True
	if (root_1 and not root_2) or (not root_1 and root_2):
		return False
	if root_1.val != root_2.val:
		return False

	if (not root_1.left and not root_1.right and not root_2.left and not root_2.right):
		return True if root_1.val == root_2.val else False
	else:
	    return twoTreesSymmetric(root_1.left, root_2.right) and twoTreesSymmetric(root_1.right, root_2.left)


root = TreeNode(1)
a_1 = TreeNode(2)
a_2 = TreeNode(2)
b_1 = TreeNode(3)
b_2 = TreeNode(4)
b_3 = TreeNode(4)
b_4 = TreeNode(3)
root.left = a_1
root.right = a_2
a_1.left = b_1
a_1.right = b_2
a_2.left = b_3
a_2.right = b_4

print(isSymmetric(root))