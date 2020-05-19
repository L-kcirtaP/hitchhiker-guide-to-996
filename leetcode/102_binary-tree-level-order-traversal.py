from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []

        cur_level_num = 1
        next_level_num = 0
        while queue:
            top = queue[0]

            if top.left:
                queue.append(top.left)
                next_level_num += 1
            if top.right:
                queue.append(top.right)
                next_level_num += 1

            if not res:
                res.append([top.val])
            else:
                res[-1].append(top.val)

            queue.pop(0)
            cur_level_num -= 1
            if cur_level_num == 0:
                if next_level_num:
                    res.append([])
                cur_level_num = next_level_num
                next_level_num = 0
        return res

root = TreeNode(3)
a1 = TreeNode(9)
a2 = TreeNode(20)
b1 = TreeNode(15)
b2 = TreeNode(7)
root.left = a1
root.right = a2
a2.left = b1
a2.right = b2

s = Solution()
print(s.levelOrder(root))
