# -*- coding:utf-8
"""
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。
 
示例 1:

输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
示例 2:

输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):

    def twoSum(self, n):
        """
        :type n: int
        :rtype: List[float]
        """
        max_res = 6 * n+1
        min_res = n
        flag = 0
        dp = [[0 for i in range(max_res)] for i in range(2)]
        for i in range(1, 7):
            dp[flag][i] = 1
        for k in range(2, n + 1):
            # 第2 到第n个骰子
            for i in range(k):
                dp[1 - flag][i] = 0
            for j in range(k, 6 * k + 1):
                try:
                    dp[1 - flag][j] = 0
                except:
                    print(j)
                k = 1
                while k >= 1 and k <= 6 and k < j:
                    # for k in range(1, 7):
                    dp[1 - flag][j] += dp[flag][j - k]
                    k += 1
            flag = 1 - flag

        total = pow(6, n)
        result = list(map(lambda x: float(x) / total, dp[flag]))
        i = 0
        while result[i] == 0.0:
            result = result[i+1:]
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum(1))
