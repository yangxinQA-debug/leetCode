# -*- coding:utf-8
"""
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
"""


class Solution(object):
    def __init__(self):
        self.results = []
        self.result = ""

    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def permutate(s, result):
            if len(s) == 0:
                self.results.append(result)
                return
            for i in range(len(s)):
                result += s[i]
                s2 = s[:i] + s[i + 1:]
                permutate(s2, result)
                result = result[:-1]
        if len(s) == 0:
            return []
        permutate(s, "")
        print(self.results)
        return list(set(self.results))


if __name__ == "__main__":
    solution = Solution()
    solution.permutation("abc")
