# -*-coding:utf-8
"""
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

示例 1:

输入: nums: [1, 1, 1, 1, 1], S: 3
输出: 5
解释:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/target-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
0-1背包解法
思想：在某个解中正数和为x，负数和的绝对值为y，则x+y=sum，x-y=S，解得x=(sum+S)/2
所以就有在nums中选择一部分数（装与不装到背包中），让其和为x（总的容量为x），此时转化为了0-1背包问题,
剩余部分数据和当然为y，所以x+y=sum，x-y=S（y中的数都去负号）

同时可有sum+S为奇数，则一定没有解的推论，因为要除以2才是x的解

此时dp数组中保存前i个数字能得到容量为j的结果的总数
"""

import numpy


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        sum = 0
        count0 = 0
        for i in range(len(nums)):
            sum += nums[i]
            if nums[i] == 0:
                count0 += 1
        if sum < S:
            return 0
        if (sum + S) % 2 == 1:
            return 0
        x = int((sum + S) / 2)
        dp = numpy.zeros([x + 1], dtype=numpy.int32)
        if nums[0] <= x:
            dp[nums[0]] = 1
        dp[0] = 1

        for i in range(1, len(nums)):
            for j in range(x, 0, -1):
                if j - nums[i] >= 0 and nums[i] != 0:
                    dp[j] = dp[j] + dp[j - nums[i]]
                else:
                    dp[j] = dp[j]
        if count0 != 0:
            print(dp[x] * pow(2, count0))
            return (dp[x] * pow(2, count0))
        else:
            print(dp[x])
            return (dp[x])


if __name__ == "__main__":
    solution = Solution()
    solution.findTargetSumWays([1, 0], 1)
