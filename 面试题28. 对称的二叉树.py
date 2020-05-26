# -*- coding:utf-8
"""
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3


示例 1：

输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：

输入：root = [1,2,2,null,3,null,3]
输出：false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        que = deque()
        que.append(root)
        while len(que):
            level = []
            for i in range(len(que)):
                popNode = que.popleft()
                if popNode != None:
                    level.append(popNode.val)
                else:
                    level.append(-1000)
                if popNode!=None:
                    if popNode.left != None:
                        que.append(popNode.left)
                    else:
                        que.append(None)
                    if popNode.right != None:
                        que.append(popNode.right)
                    else:
                        que.append(None)
            i, j = 0, len(level) - 1
            while i < j:
                if level[i] != level[j]:
                    return False
                i += 1
                j -= 1
        return True


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(3)
    solution = Solution()
    print(solution.isSymmetric(root))
