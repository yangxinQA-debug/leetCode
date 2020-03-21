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


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ##bad case: s=""
        if len(s) == 0:
            return 0
        dp = [0] * len(s)
        dp[0] = 1
        for i in range(1, len(s)):
            dp[i] = dp[i - 1] + 1
            j = i - 1
            while j >= 0:
                if s[j] != s[i]:
                    j -= 1
                    continue
                r = i
                l = j
                flag = True
                while (r >= l):
                    if (s[r] != s[l]):
                        flag = False
                        break
                    r -= 1
                    l += 1
                if flag:
                    dp[i] += 1
                j -= 1

        print(dp[len(s) - 1])
        return dp[len(s) - 1]


if __name__ == "__main__":
    solution = Solution()
    solution.countSubstrings("aba")
