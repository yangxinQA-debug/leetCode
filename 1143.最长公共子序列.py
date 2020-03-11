# -*- coding:utf-8
"""
给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

若这两个字符串没有公共子序列，则返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import numpy

class Solution(object):
    """
    1）dp[i][j] 表示str1[0~i]和str2[0~j]的最长公共子序列长度
    2）递归关系：
       str1[i]!=str2[j] 时，dp[i][j]=max{dp[i-1][j],dp[i][j-1]}
       str1[i]==str2[j] 时,dp[i][j] = dp[i-1][j-1]+1
    """

    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = numpy.zeros([len(text1), len(text2)], dtype=numpy.int32)
        count1 = 0
        count2 = 0
        ## 初始化第0行和第0列
        for i in range(len(text1)):
            if (text1[i] == text2[0]):
                count1 = 1
            if count1 == 1:
                dp[i][0] = 1
            else:
                dp[i][0] = 0
        for j in range(len(text2)):
            if (text2[j] == text1[0]):
                count2 = 1
            if count2 == 1:
                dp[0][j] = 1
            else:
                dp[0][j] = 0
        ##递归计算
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if (text1[i] == text2[j]):
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        print(dp[len(text1) - 1][len(text2) - 1])
        return dp[len(text1) - 1][len(text2) - 1]




if __name__ == "__main__":
    solution = Solution()
    solution.longestCommonSubsequence("lcnqdmvsdopkvqvejijcdyxetuzonuhuzkpelmva",
                                      "bklgfivmpozinybwlovcnafqfybodkhabyrglsnen")
