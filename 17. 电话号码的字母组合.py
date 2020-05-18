# -*- coding:utf-8
"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map_digits = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        results = []

        def findCombinations(index, digits, s):
            """
            :param index: digit[index]表示遍历到index位置的字母
            :param digits: 数字输入串
            :param s:
            :return:
            """
            if index == len(digits):
                results.append(s)
                return
            c = digits[index]
            chars = map_digits[c]
            for i in chars:
                findCombinations(index + 1, digits, s + i)

        if digits == "":
            return []

        findCombinations(0, digits, "")
        print(results)
        return results


if __name__ == "__main__":
    solution = Solution()
    solution.letterCombinations("23")
