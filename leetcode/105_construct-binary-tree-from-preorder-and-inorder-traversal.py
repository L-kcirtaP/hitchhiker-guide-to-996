class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(preorder, inorder) -> TreeNode:
	if not preorder:
		return None
	node = TreeNode(preorder[0])
	pos = inorder.index(preorder[0])
	
	node.left = buildTree(preorder[1:1+pos], inorder[0:pos])
	node.right = buildTree(preorder[1+pos:], inorder[pos+1:])
	return node


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root = buildTree(preorder, inorder)
print(root.val)