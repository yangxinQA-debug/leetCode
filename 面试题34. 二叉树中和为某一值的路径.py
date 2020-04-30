# -*-coding:utf-8
"""
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

 

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        paths = []
        add = 0
        routes = []
        self.preOrder(root, sum, paths, add, routes)
        return routes

    def preOrder(self, root, sum, paths, add, routes):
        if root == None:
            return
        paths.append(root)
        add += root.val
        if root.left == None and root.right == None:
            if add == sum:
                print(paths)
                route = []
                for i in paths:
                    route.append(i.val)
                routes.append(route)
                add -= root.val
                paths.pop()
                return paths
            # else:
            #     add -= root.val
            #     paths.pop()
        self.preOrder(root.left, sum, paths, add, routes)
        self.preOrder(root.right, sum, paths, add, routes)
        add -= root.val
        paths.pop()


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(12)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(7)
    print(solution.pathSum(root, 22))
