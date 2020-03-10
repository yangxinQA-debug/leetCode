# -*- coding:utf-8
"""
300. 最长上升子序列
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
"""

"""
时间复杂度O(n^2)
"""

import numpy
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dp = numpy.zeros(len(nums), dtype=numpy.int32)
        dp[0] = 1
        for i in range(1, len(nums)):
            max = 0
            j = 0
            while (j < i):
                if (nums[j] < nums[i] and max < dp[j]):
                    max = dp[j]
                j += 1
            dp[i] = max + 1
        print(dp)
        # 获取最长上升序列
        list = []
        maxlen = dp[0]
        max_index = 0
        ## 找到最大值所在的位置
        for k in range(len(dp)):
            if (dp[k] > maxlen):
                maxlen = dp[k]
                max_index = k
        list.append(nums[max_index])

        m = max_index - 1
        while (maxlen > 1):
            if dp[m] == maxlen - 1:
                list.append(nums[m])
                maxlen -= 1
            m -= 1
        print(list[::-1])
        return len(list[::-1])


if __name__ == "__main__":
    solution = Solution()
    solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
