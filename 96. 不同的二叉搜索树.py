# -*-coding:utf-8
"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-binary-search-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
遍历以1为根，2为根。。。k为根的情况
f(k)表示k 个节点构成搜索树的方法。 以j为根，1~j-1 构成左子树，j+1~k构成右子树
f(0) = 1
f(1) = 1
f(2) = 2
f(k) = sum(f(i)*f(k-1-i))(i =0 ...k-1)
"""


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [-1] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for k in range(2, n + 1):
            sum = 0
            for i in range(0, k ):
                sum += dp[i] * dp[k - i - 1]
            dp[k] = sum
        print(dp[n])
        return dp[n]


if __name__ == "__main__":
    solution = Solution()
    solution.numTrees(2)
