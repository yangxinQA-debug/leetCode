# -*-coding:utf-8
"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        end = len(postorder) - 1
        start = 0
        return self.judgePostOrder(postorder, start, end)

    def judgePostOrder(self, postorder, start, end):
        if start >= end:
            return True
        root = postorder[end]
        for i in range(start, end):
            if postorder[i] > root:
                break
        if i == end - 1:
            return self.judgePostOrder(postorder,start,end-1)
        # start~i-1 为左子树，i~end-1为右子树
        for j in range(i, end):
            if postorder[j] <= root:
                return False
        left = self.judgePostOrder(postorder, start, i - 1)
        right = self.judgePostOrder(postorder, i, end - 1)
        return left and right


if __name__ == "__main__":
    solution = Solution()
    print(solution.verifyPostorder([5, 2, -17, -11, 25, 76, 62, 98, 92, 61]))
