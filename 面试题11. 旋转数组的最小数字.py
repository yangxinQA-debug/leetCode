# -*- coding:utf-8
"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0
"""


class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        if len(numbers) == 0:
            return None
        lastnum = numbers[len(numbers) - 1]
        return self.search(numbers, 0, len(numbers) - 1)

    def search(self, numbers, l, r):
        if l == r:
            return numbers[l]
        m = (l + r) // 2
        if numbers[m] < numbers[r]:
            r = m
        elif numbers[m] > numbers[r]:
            l = m + 1
        elif numbers[m] == numbers[r]:
            r = r - 1
        return self.search(numbers, l, r)


if __name__ == "__main__":
    solution = Solution()
    result = solution.minArray([2,2,2,0,1])
    print(result)
