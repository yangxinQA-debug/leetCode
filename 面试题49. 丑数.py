# -*- coding:utf-8
"""
我们把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/chou-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
题解：
https://www.bilibili.com/video/BV1T7411t7Dm?from=search&seid=12906184319454580644
"""


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1]
        p2 = p3 = p5 = 0
        for i in range(0, n):
            dpi = min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)
            dp.append(dpi)
            while dp[p2] * 2 <= dpi:
                p2 += 1
            while dp[p3] * 3 <= dpi:
                p3 += 1
            while dp[p5] * 5 <= dpi:
                p5 += 1
        return dp[n-1]

if __name__ == "__main__":
    solution = Solution()
    print(solution.nthUglyNumber(10))
