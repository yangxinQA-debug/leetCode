"""
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 

示例 1:

输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
示例 2:

输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。
示例 3:

输入: amount = 10, coins = [10]
输出: 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change-2
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    """
    1)定义数组dp[len(coins)][amount+1],dp[i][j]表示，使用coins[0]~coins[i]组成j的方法数
    2）初始化数组，dp[0][j]= j%coins[0]==0?  dp[0][j]=1 :dp[0][j]=0
       dp[i][0] = 1
    3)递归关系 dp[i][j] = dp[i-1][j]+dp[i-1][j-coin[i]]+dp[i-1][j-coins[i]*2]+...+dp[i-1][j-coins[i]*k]
                       = dp[i-1][j]+dp[i][j-coins[i]]
    4)空间压缩：用一行记录:
              dp[i] =dp[j-coins[i]](此处为更新过得第i 行)+dp[i]（此处为未更新的第i-1行）
     """

    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if (len(coins) == 0 and amount == 0):
            return 1
        elif (len(coins) == 0 and amount != 0):
            return 0
        dp = [0] * (amount + 1)
        for i in range(0, amount + 1):
            if (i % coins[0] == 0):
                dp[i] = 1

        for i in range(1, len(coins)):
            for k in range(1, amount + 1):
                if (k - coins[i] >= 0):
                    left = dp[k - coins[i]]
                else:
                    left = 0
                dp[k] = left + dp[k]

        print(dp[amount])
        return dp[amount]


if __name__ == "__main__":
    solution = Solution()
    solution.change(amount = 10, coins = [10] )
