# -*-coding:utf-8
"""

请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
镜像输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.mirrorTree(root.left)
        self.mirrorTree(root.right)
        return root


if __name__ == "__main__":
    root = [4, 2, 7, 1, 3, 6, 9]

    solution = Solution()
    solution.mirrorTree()
