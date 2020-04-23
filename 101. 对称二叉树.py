# -*-coding:utf-8
"""
给定一个二叉树，检查它是否是镜像对称的。

 

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
题解：
https://leetcode-cn.com/problems/symmetric-tree/solution/dui-cheng-er-cha-shu-by-leetcode/
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.ismirror(root.left, root.right)

    def ismirror(self, a, b):
        """
        判断a,b 为根的两颗树，是否互为镜像树
        :param a:
        :param b:
        :return:
        """
        if a == None and b == None:
            return True
        if a == None or b == None:
            return False
        return (a.val == b.val) and self.ismirror(a.left, b.right) and self.ismirror(a.right, b.left)
