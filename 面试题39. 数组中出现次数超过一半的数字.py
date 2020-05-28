# -*- coding:utf-8
"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:

输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2


限制：

1 <= 数组长度 <= 50000

"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        votes = 0
        x =0
        for i in nums:
            if votes == 0:
                x = i
            if i == x:
                votes += 1
            else:
                votes -= 1
        return x
if __name__ == "__main__":
    solution = Solution()
    print(solution.majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2]))
