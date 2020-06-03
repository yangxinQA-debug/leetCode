# -*- coding:utf-8
"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import copy


class Solution(object):
    def __init__(self):
        self.result = []

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        size = len(nums)
        nums = sorted(nums)
        self.dfs(nums, size, 0, [])
        return self.result
    # 使用回溯法，每次只添加后面的数字
    def dfs(self, nums, size, index, res):
        res_str = copy.deepcopy(res)
        self.result.append(res_str)
        for i in range(index, size):
            res.append(nums[i])
            self.dfs(nums, size, i + 1, res)
            res.pop()


if __name__ == "__main__":
    solution = Solution()
    print(solution.subsetsWithDup([1, 2, 3]))
