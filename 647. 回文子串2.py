# -*- coding:utf-8
"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

示例 1:

输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".
示例 2:

输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
"""

"""
 1)定义数组dp[i][j] 表s[i]~s[j]是否是回文串
 2)初始化 dp[i][i] = True
 3)状态转移方程：
    if s[i] == s[j]:   dp[i][j] = dp[i+1][j-1]
    else s[i] != s[j]:  dp[i][j] = False
  4）只遍历矩阵的右上角，判断s[i]到s[j]（i<j）,是否是回文子串
  https://www.bilibili.com/video/av78687272?from=search&seid=930518925619994112
"""


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        n = len(s)
        if n == 0:
            return 0
        dp = [[False for i in range(n)] for i in range(n)]
        # 长度为1 的回文串
        for i in range(n):
            dp[i][i] = True
            count += 1
        # 长度为2 ，两个字母相同为回文串
        for i in range(n-1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1
        # 长度大于等于3时：
        for size in range(3, n+1):
            for i in range(n - size+1):
                j = i + size - 1
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
                if dp[i][j]:
                    count += 1
        print(count)
        return count




if __name__ == "__main__":
    solution = Solution()
    solution.countSubstrings("aaa")
