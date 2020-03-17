# -*-coding:utf-8
"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2:
输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if len(nums) % 2 == 0:
            even = True
        else:
            even = False
        s1 = 0
        s2 = 0
        if even:
            i1 = 0
            i2 = 1
            while i1 <= n - 2:
                s1 += nums[i1]
                i1 += 2
            while i2 <= n - 1:
                s2 += nums[i2]
                i2 += 2
        else:
            i1 = 0
            i2 = 1
            while i1 <= n - 1:
                s1 += nums[i1]
                i1 += 2
            while i2 <= n - 2:
                s2 += nums[i2]
                i2 += 2
        print(max(s1, s2))
        return max(s1, s2)

if __name__ == "__main__":
    input = [2,7,9,3,1]
    solution = Solution()
    solution.rob(input)
