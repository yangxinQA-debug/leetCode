# -*-coding:utf-8
"""
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
https://leetcode-cn.com/problems/longest-valid-parentheses/solution/qiao-miao-de-dong-tai-gui-hua-by-byb_boy/
"""
"""
num[i] == "("时，dp[i]=0
num[i] == ")"时，if num[i-1]=="(": dp[i] = dp[i-2]+2
num[i] == ")"时，if num[i-1]==")" and num[i-1-dp[i-1]]=='(' : dp[i] = dp[i-1]+2+dp[i-2-dp[i-1]]
num[i] == ")"时，if num[i-1]==")" and num[i-1-dp[i-1]]==')' : dp[i]=0 
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        max_len = 0
        dp = [0] * len(s)
        dp[0] = 0
        for i in range(1, len(s)):
            if s[i] == '(':
                dp[i] = 0
            elif s[i] == ")" and s[i - 1] == "(":
                dp[i] = dp[i - 2] + 2
            elif s[i] == ")" and s[i - 1] == ")" and i - 1 - dp[i - 1] >= 0 and s[i - 1 - dp[i - 1]] == "(":
                dp[i] = dp[i - 1] + 2 + dp[i - 2 - dp[i - 1]]
            elif s[i] == ")" and s[i - 1] == ")" and i - 1 - dp[i - 1] <0:
                dp[i] = 0
            elif s[i] == ")" and s[i - 1] == ")" and s[i - 1 - dp[i - 1]] == ")":
                dp[i] = 0
            if dp[i] > max_len:
                max_len = dp[i]

        print(max_len)
        return max_len


if __name__ == "__main__":
    solution = Solution()
    solution.longestValidParentheses("(()))())(")
