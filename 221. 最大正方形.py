# -*- coding:utf-8
"""
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4
"""
"""
dp[i][j]表示以i，j 为右下角的，全1矩形的最长边长
 if m[0][j] ==1 : dp[0][j] =1
 if m[i][0] ==1 : dp[i][0] =1
2)状态转移方程：
  if m[i][j] == 1: 
       dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
  else:
       dp[i][j] = 0
"""
import numpy


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        h = len(matrix)
        w = len(matrix[0])
        dp = numpy.zeros([h, w], dtype=numpy.int32)
        maxSize = 0
        for i in range(w):
            if matrix[0][i] == "1":
                dp[0][i] = 1
                if dp[0][i] > maxSize:
                    maxSize = dp[0][i]

        for j in range(h):
            if matrix[j][0] == "1":
                dp[j][0] = 1
                if dp[j][0] > maxSize:
                    maxSize = dp[j][0]

        for i in range(1, h):
            for j in range(1, w):
                if matrix[i][j] == "0":
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    if dp[i][j] > maxSize:
                        maxSize = dp[i][j]

        print("maxSize: " + str(maxSize))
        return int(maxSize * maxSize)


if __name__ == "__main__":
    solution = Solution()
    # solution.maximalSquare([[1, 0, 1, 0, 0],
    #                         [1, 0, 1, 1, 1],
    #                         [1, 1, 1, 1, 1],
    #                         [1, 0, 0, 1, 0]])
    # solution.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
    solution.maximalSquare([["0", "1"]])
