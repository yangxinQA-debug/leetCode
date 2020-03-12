# -*-coding:utf-8
"""
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
示例 1:

输入: word1 = "horse", word2 = "ros"
输出: 3
解释:
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2:

输入: word1 = "intention", word2 = "execution"
输出: 5
解释:
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import numpy

"""
字符串前加入''，处理''的特殊case

dp[i][j]表示从串str1[0~i]编辑到str[0~j]的距离
1）初始化dp[0][j]=j,dp[i][0]=i
2)状态转移方程：
     if str1[i]!=str2[j]:  dp[i][j]= min(dp[i][j-1]+1,dp[i-1][j]+1,dp[i-1][j-1]+1)
     else: dp[i][j] = dp[i-1][j-1]
     
     str1[i]!=str2[j]:
        str1[0~i]编辑到str2[0~j] 的方法1， str1[0~i]删除str1[i],str1[i-1]编辑为str2[j]. dp[i][j]=dc+dp[i-1][j]
        str1[0~i]编辑到str2【0~j]的方法2 ，str1[0~i]编辑到str2[j-1],添加str2[j],dp[i][j] = dp[i][j-1]+ic
        str1[0~i]编辑到str2【0~j]的方法3， str1[0~i-1]编辑到str2[j-1],将str2[j] 替换为str1[i], dp[i][j] = dp[i-1][j-1]+1
     str1[i]==str2[j]:
        str1[0~i]编辑到str2[0~j] 的方法: str1[0~i-1]编辑为str2[0~j-1]， dp[i][j] = dp[i-1][j-1]
     
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1 = len(word1) + 1
        len2 = len(word2) + 1
        dp = numpy.zeros((len1, len2), dtype=numpy.int32)
        word1 = " " + word1
        word2 = " " + word2
        for j in range(len2):
            dp[0][j] = j
        for i in range(len1):
            dp[i][0] = i

        for i in range(1, len1):
            for j in range(1, len2):
                if (word1[i] != word2[j]):
                    dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1)
                else:
                    dp[i][j] = dp[i - 1][j - 1]
        print(dp[len1 - 1][len2 - 1])
        result = dp[len1 - 1][len2 - 1]
        return result


if __name__ == "__main__":
    solution = Solution()
    solution.minDistance(word1="intention", word2="execution")
