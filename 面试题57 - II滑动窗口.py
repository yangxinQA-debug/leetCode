# -*- coding:utf-8
"""
和为s的连续正数序列

输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
输入：target = 9
输出：[[2,3,4],[4,5]]
"""


class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        i = 1
        j = 1
        while (i <= j and j < target):
            sum = (i + j) * (j - i + 1) / 2
            if (sum < target):
                j += 1
            elif (sum > target):
                i += 1
            else:
                list = []
                for k in range(i, j + 1):
                    list.append(k)
                result.append(list)
                j += 1
        print(result)
        return result


if __name__ == "__main__":
    solution = Solution()
    solution.findContinuousSequence(15)
