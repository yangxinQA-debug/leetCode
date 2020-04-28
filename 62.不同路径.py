# -*-coding:utf-8
"""
62. 不同路径
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？
"""
import numpy


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if (m == 0 or n == 0):
            return 0
        dp = numpy.zeros([m, n], dtype=numpy.int32)
        # 初始化
        for i in range(0, m):
            dp[i][0] = 1
        for j in range(0, n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        print(dp[m - 1][n - 1])
        return int(dp[m - 1][n - 1])


if __name__ == "__main__":
    solution = Solution()
    solution.uniquePaths(m=7, n=3)
