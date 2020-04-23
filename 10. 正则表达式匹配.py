# -*-coding:utf-8
"""
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/regular-expression-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = 0
        j = 0
        while i < len(p) and j < len(s):
            if (p[i] == s[j] and i < len(p) - 1 and p[i + 1] != '*') or (p[i] == s[j] and i == len(p) - 1):
                i += 1
                j += 1
            elif p[i] == '.':
                i += 1
                j += 1
            elif i < len(p) - 1 and p[i + 1] == '*' and p[i] != s[j]:
                i += 2
            elif i < len(p) - 1 and p[i + 1] == '*' and p[i] == s[j]:
                i += 2
                j += 1
            elif p[i] != p[j]:
                print(False)
                return False
        if i == len(p) and j == len(s):
            print(True)
            return True
        else:
            print(False)
            return False


if __name__ == "__main__":
    solution = Solution()
    s = "aa"
    p = "a*"
    solution.isMatch(s, p)