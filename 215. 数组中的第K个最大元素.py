# -*- coding:utf-8
"""

在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
"""
import random


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 找到第k个最大元素==找到n-k位置的元素
        return self.partitionArray(nums, 0, len(nums) - 1, k)

    def partitionArray(self, nums, l, h, k):
        index = self.partition(nums, l, h)
        while index != len(nums) - k:
            if index < len(nums) - k:
                index = self.partition(nums, index + 1, h)
            elif index > len(nums) - k:
                index = self.partition(nums, l, index - 1)
            else:
                return nums[index]

    def partition(self, nums, l, h):
        tmp = nums[l]
        rand = random.randint(l, h)
        nums[l] = nums[rand]
        nums[rand] = tmp
        tmp = nums[l]
        p, q = l, h
        while p < q:
            while nums[q] >= tmp and p < q:
                q -= 1
            nums[p] = nums[q]
            while nums[p] <= tmp and p < q:
                p += 1
            nums[q] = nums[p]
        nums[p] = tmp
        return p


if __name__ == "__main__":
    solution = Solution()
    print(solution.findKthLargest([3, 2, 1, 5, 6, 4], k=2))
