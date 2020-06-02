# -*- coding:utf-8
"""
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 2：

输入：m = 3, n = 1, k = 0
输出：1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    visited = set()

    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        return self.dfs(0, 0, m, n, k)

    def edge(self, l):
        s = 0
        while l:
            s += l % 10
            l = l // 10
        return s

    def dfs(self, i, j, m, n, k):
        """
        :param i: 查找的初始纵坐标
        :param j: 查找的初始横坐标
        :param m:
        :param n:
        :param k:
        :return:
        """
        if i >= m or j >= n or i < 0 or j < 0 or self.edge(i) + self.edge(j) > k or (i, j) in self.visited:
            return 0
        self.visited.add((i, j))
        b = self.dfs(i + 1, j, m, n, k)
        r = self.dfs(i, j + 1, m, n, k)
        l = self.dfs(i, j - 1, m, n, k)
        t = self.dfs(i - 1, j, m, n, k)
        return 1 + b + r + l + t


if __name__ == "__main__":
    solution = Solution()
    result = solution.movingCount(m=1, n=2, k=1)
    print(result)
