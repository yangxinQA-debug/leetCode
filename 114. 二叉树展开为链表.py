# -*-coding:utf-8
"""
给定一个二叉树，原地将它展开为链表。

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    将左子树插入到右子树的地方
    将原来的右子树接到左子树的最右边节点
    考虑新的右子树的根节点，一直重复上边的过程，直到新的右子树为 null
    """

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        r = root
        # while p.right != None:
        #     p = p.right

        while (r != None):
            if r.left != None:
                tmp = r.right
                r.right = r.left
                rightest = self.get_rightest_node(r.left)
                rightest.right = tmp
                r.left = None
            r = r.right
        return root

    def get_rightest_node(self, root):
        p = root
        while p.right != None:
            p = p.right
        return p


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)
    root.right.left = None
    solution = Solution()
    solution.flatten(root)
