# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return 
        
        return self.invertTreeCore(root, root.left, root.right)


    def invertTreeCore(self, root: TreeNode, left: TreeNode, right: TreeNode) -> TreeNode:
        if left:
            left = self.invertTreeCore(left, left.left, left.right)
        if right:
            right = self.invertTreeCore(right, right.left, right.right)
        root.left, root.right = right, left
        
        return root
