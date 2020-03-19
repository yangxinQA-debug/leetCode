class Solution:
    def findTargetSumWays(self, nums, S) :
        # 首先统计一下0的个数，背包问题是没有0这个容量的, 由于每个0都有+-而不影响结果，所最后的结果需要乘以2**count_0
        count_0 = 0
        for num in nums:
            if num == 0:
                count_0 += 1
        for i in range(count_0):
            nums.remove(0)

        if (S + sum(nums)) % 2 == 1 or sum(nums) < S:
            return 0
        target = (S + sum(nums)) // 2  # 那么和518 号问题：零钱兑换II基本一样了（但是是01背包问题）
        n = len(nums)

        dp = [[0] * (target + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        # 但是空间优化的时候不需要考虑0的问题了，具体看空间优化提交结果
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if nums[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
        return dp[n][target] * (2 ** count_0)

if __name__ == "__main__":
    solution = Solution()
    # result = solution.findTargetSumWays(nums= [1, 1, 1, 1, 1], S= 3)
    result=solution.findTargetSumWays([1000], -1000)
    print(result)