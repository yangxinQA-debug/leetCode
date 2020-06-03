# -*- coding:utf-8
"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets-ii
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
        if nums == []:
            return []
        size = len(nums)
        used = [False for i in range(len(nums))]
        nums = sorted(nums)
        self.dfs(nums, size, 0, [], used)
        return self.result

    def dfs(self, nums, size, index, res, used):
        res_str = copy.deepcopy(res)
        self.result.append(res_str)
        for i in range(index, size):
            if i >= 1 and nums[i] == nums[i - 1] and used[i - 1] == False:
                continue
            res.append(nums[i])
            used[i] = True
            self.dfs(nums, size, i + 1, res, used)
            res.pop()
            used[i] = False


if __name__ == "__main__":
    solution = Solution()
    print(solution.subsetsWithDup([1, 1]))
