# -*- coding:utf-8
"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import numpy
from numpy import int32


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s2 = s[::-1]
        dp = numpy.zeros((len(s), len(s2)), dtype=int32)
        if s == "":
            print("")
            return ""
        for i in range(len(s)):
            if (s[i] == s2[0]):
                dp[i][0] = 1
            else:
                dp[i][0] = 0

        for j in range(len(s2)):
            if (s2[j] == s[0]):
                dp[0][j] = 1
            else:
                dp[0][j] = 0

        max = 0
        index = 0
        for i in range(1, len(s)):
            for j in range(1, len(s2)):
                if (s[i] == s2[j]):
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
                ## 判断是否是回文串：
                if (dp[i][j] > max):
                    before = len(s) - 1 - j  # 在s2中s[j]的起始位置
                    reverse_position = before + dp[i][j] - 1  # 在s2中s[j]的镜像位置
                    if reverse_position == i:  # 和镜像位置的数值相同时，做长度标记
                        max = dp[i][j]
                        index = i
        if index == 0 and max == 0:
            print(s[0])
            return s[0]
        elif index != 0 and max != 0:
            print(s[index - max + 1:index + 1])
            return s[index - max + 1:index + 1]


if __name__ == "__main__":
    solution = Solution()
    solution.longestPalindrome("babad")
