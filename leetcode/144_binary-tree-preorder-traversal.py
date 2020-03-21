# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def preorderTraversal(root: TreeNode):
    result = []
    traverse(root, result)
    return list(filter(lambda x: x != None, result))

def traverse(node, result):
    if not node:
        return
    result += [node.val]
    result += [traverse(node.left, result)]
    result += [traverse(node.right, result)]
