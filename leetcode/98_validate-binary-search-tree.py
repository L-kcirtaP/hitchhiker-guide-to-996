# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isValidBST(root: TreeNode) -> bool:
	return isValidBSTCore(root, None, None)

def isValidBSTCore(root: TreeNode, lower: int, upper: int) -> bool:
	result = True
	if not root:
		return result
	if lower is not None:
		result &= root.val > lower
	if upper is not None:
		result &= root.val < upper

	if root.left:
		result &= isValidBSTCore(root.left, lower, root.val)
	
	if root.right:
		result &=  isValidBSTCore(root.right, root.val, upper)

	return result

root = TreeNode(0)
c = TreeNode(-1)
root.right = c
print(isValidBST(root))
