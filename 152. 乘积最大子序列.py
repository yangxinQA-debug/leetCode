# -*- coding:utf-8
"""
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
1) max[i]: 表示以i 为结尾的*连续*数组乘积的最大值
2) min[i]: 表示以i 为结尾的*连续*数组乘积的最小值
2）递归: max[i] = max(nums[i],max[i-1]*nums[i],min[i-1]*nums[i])
        min[i] = min(nums[i],min[i-1]*nums[i],max[i-1]*nums[i])
4)maxresult 记录每个maxProduct 比较后的最大值
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxResult = nums[0]
        maxProduct = [0]*(len(nums))
        minProduct = [0]*(len(nums))
        maxProduct[0] = nums[0]
        minProduct[0] = nums[0]
        for i in range(1, len(nums)):
            maxProduct[i] = max(nums[i], maxProduct[i - 1] * nums[i], minProduct[i - 1] * nums[i])
            minProduct[i] = min(nums[i], minProduct[i - 1] * nums[i], maxProduct[i - 1] * nums[i])
            maxResult = max(maxResult,maxProduct[i])
        print(maxResult)
        return maxResult

if __name__ == "__main__":
    nums = [-2, 3, -4]
    solution = Solution()
    solution.maxProduct(nums)
