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
时间复杂度O(logn)
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
        """
        1)ends 数组记录递增序列的最小结尾值，ends[k]=a ，表示以长度为k+1的递增子序列的最小结尾为a
        2)遍历nums数组，nums[k]>ends[r]结尾值时，表示num[k]可以做为最长子序列的结尾值。
        3）遍历nums数组，nums[k]<ends[r]结尾时，在ends[l]~ends[r]区间内寻找第一个大于nums[k]的位置，并用nums[k]替换这个位置的值
        """
        # ends 数组初始化为0
        res = 0
        r = -1
        ends = numpy.zeros(len(nums), dtype=numpy.int32)
        dp = numpy.zeros(len(nums), dtype=numpy.int32)
        for i in nums:
            l = 0
            found = 0
            while (l <= r):
                mid = int((l + r) / 2)
                if (i > ends[r]):
                    ends[r + 1] = i
                    r += 1
                    res = r
                    found = 1
                    break
                elif (i < ends[mid]):
                    res = r + 1
                    r = mid - 1
                elif (i > ends[mid]):
                    l = mid + 1
                else:
                    found = 1
                    break
            if found == 0:
                ends[r + 1] = i
                r += 1
                r = res
            index = numpy.argwhere(ends == 0)
            length = (int(index[0]))
            r = length - 1
        print(ends[0:r + 1])
        index = numpy.argwhere(ends == 0)
        print(res)
        return res


if __name__ == "__main__":
    solution = Solution()
    solution.lengthOfLIS([0])
