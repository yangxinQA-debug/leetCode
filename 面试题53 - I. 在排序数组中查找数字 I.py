# -*- coding:utf-8
"""

统计一个数字在排序数组中出现的次数。



示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0


限制：

0 <= 数组长度 <= 50000
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (i + j) / 2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                print(mid)
                count = 1
                k = 1
                l = 1
                while nums[mid + k] == nums[mid] and mid + k <= len(nums) - 1:
                    count += 1
                    k += 1
                    print(k)
                while nums[mid - l] == nums[mid] and mid - l >= 0:
                    count += 1
                    l += 1
                    print(l)
                return count
        return 0


if __name__ == "__main__":
    solution = Solution()
    solution.search([1], 1)
