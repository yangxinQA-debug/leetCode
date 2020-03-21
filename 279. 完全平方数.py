# -*- coding:utf-8
"""
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
示例 1:

输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.
示例 2:


输入: n = 13
输出: 2
解释: 13 = 4 + 9.
"""
"""
dp[i] 表示组成和为i的完全平方数的最小个数
1）初始化dp[0] = 0,dp[1] =1
2)状态转移方程： dp[i] =i 
              for j in range(square(i)):
                  dp[i] = min(dp[i],dp[i-j*j]+1)
"""

import math


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        for i in range(n+1):  # 从小到大求dp[i]数组
            dp[i] = i  # 初始化dp[i] 最多为i个1 组成
            for j in range(int(math.sqrt(i)+1)):
                # 更新dp[i]的值，如果dp[i-j*j]+1更新，替换为新值。dp[i-j*j]+1 表示由 j 和组成i-j*j的数，一起组合成i
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        print( dp[n])
        return dp[n]

if __name__ == "__main__":
    solution = Solution()
    solution.numSquares(13)
