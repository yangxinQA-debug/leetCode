# -*-coding:utf-8
"""
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        root = self.build_recrusive(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)
        return root

    def build_recrusive(self, preorder, inorder, pl, pr, il, ir):
        if pl > pr:
            return None
        root = TreeNode(preorder[pl])
        root_index_inorder = inorder.index(preorder[pl])
        len_left_child = root_index_inorder - il
        ## preorder 的左子树坐标：pl+1~pl+len_left_child
        ## preorder 的右子树坐标：pl+len_left_child+1~pr

        ## inorder 的左子树坐标：il~root_index_inorder-1
        ## inorder 的右子树坐标：root_index_inorder+1~ir

        root.left = self.build_recrusive(preorder, inorder, pl + 1, pl + len_left_child, il, root_index_inorder - 1)
        root.right = self.build_recrusive(preorder, inorder, pl + len_left_child + 1, pr, root_index_inorder + 1, ir)
        return root

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        queue = deque([root])
        level = 0
        levels = []
        while len(queue):
            levels.append([])
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                levels[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        print(levels)
        return levels


if __name__ == "__main__":
    solution = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = solution.buildTree(preorder, inorder)
    levels = solution.levelOrder(root)
    print(levels)
