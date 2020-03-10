# -*- coding:utf-8
"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
   构造dp矩阵
   p(i,ammout)表示以货币arr[0],arr[1]...arr[i]组合amount的方法数
   p(i,amout)=min{p(i-1,amount),p(i-1,amount-arr[i])+1,p(i-1,amount-arr[i]*2)+2,...P(i-1,amoutt-k*arr[0])+k}|{k>==0}
   以i，amount为递归条件，组成dp数组。
"""
"""
 递归式推导：
 dp[i,j] = min{dp[i-1][j-k*coins[i]]+k|k>=0}
              = min{dp[i-1][j],min{dp[i-1][j-l*coins[i]+l|l>1}}
              = min{dp[i-1][j],min{dp[i-1][(j-coins[i])-(l-1)*coins[i]+l-1}+1|l>1}
              = min{dp[i-1][j],dp[i][j-coins[i]]+1}
"""
"""
  空间压缩优化
  使用dp[] 一维数组，dp[i][amount-coins[i]]优先更新为i 行的值，dp[i-1][amount]还保留i-1行的值，可用一维数组实现计算
"""
import numpy


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        max = 10000000000
        dp = [max] * (amount + 1)

        for i in range(1, amount + 1):
            # if (i - coins[0] >0 and i - coins[0] < amount and dp[i - coins[0]] != max):
            #     dp[i] = dp[i - coins[0]] + 1
            if (i % coins[0] == 0):
                dp[i] = i / coins[0]
        dp[0] = 0

        for i in range(1, len(coins)):
            for j in range(1, amount + 1):
                left = max
                if (j - coins[i] >= 0 and dp[j - coins[i]] != max):
                    left = dp[j - coins[i]] + 1
                dp[j] = min(left, dp[j])

        if (dp[amount - 1] != max):
            print(dp[amount])
            return int(dp[amount])
        else:
            return -1


if __name__ == "__main__":
    solution = Solution()
    solution.coinChange(coins=[1, 2, 5], amount=11)
