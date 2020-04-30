"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false
示例 2：

输入：A = [3,4,5,1,2], B = [4,1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        return self.preOrder(A, B)

    def preOrder(self, A, B):
        if A == None:
            return False
        if B == None:
            return False
        if A.val == B.val and self.judge(A, B):
                return True
        else:
            left = self.preOrder(A.left, B)
            right = self.preOrder(A.right, B)
            if left or right:
                return True
            else:
                return False

    def judge(self, A, B):
        if A == None and B == None:
            return True
        if A != None and B == None :
            return True
        if A == None and B != None:
            return False
        if A.val != B.val:
            return False
        if A.val == B.val:
            judgeleft = self.judge(A.left, B.left)
            judgeright = self.judge(A.right, B.right)
            return judgeleft and judgeright


if __name__ == "__main__":
    A = TreeNode(1)
    A.left = TreeNode(0)
    A.right = TreeNode(1)
    A.left.left = TreeNode(-4)
    A.left.right = TreeNode(-3)

    B = TreeNode(1)
    B.left = TreeNode(-4)
    solution = Solution()
    print(solution.preOrder(A, B))
