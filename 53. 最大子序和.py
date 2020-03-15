# -*-coding:utf-8
"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    """
    dp[i]表示以i为结尾的连续数组和的最大值
    """

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max((dp[i - 1] + nums[i]), nums[i])
            if (dp[i] > maxSum):
                maxSum = dp[i]
        print(maxSum)
        return maxSum


if __name__ == "__main__":
    solution = Solution()
    solution.maxSubArray([1, 2])
