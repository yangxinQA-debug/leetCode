# -*- coding:utf-8
"""

"""


class Solution(object):
    def longestPalindrome(self, s,s2):
        """
        :type s: str
        :rtype: str
        """

        # 找到s 和 s2 的最长公共子串
        row = 0
        col = len(s2) - 1
        max = 0
        index = 0
        while (row < len(s)):
            i = row
            j = col
            length = 0
            while (i < len(s) and j < len(s2)):
                if (s[i] != s2[j]):
                    length = 0
                else:
                    length += 1
                    if length > max:
                        max = length
                        index = i
                i += 1
                j += 1
            if (col > 0):
                col -= 1
            else:
                row += 1
        print (s[index-max+1:index+1])
        return s[index-max+1:index+1]


if __name__ == "__main__":
    solution = Solution()
    solution.longestPalindrome("aacdefcaa","ercde")
