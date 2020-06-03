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

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        size = len(nums)
        self.dfs([], nums, 0, size)
        return self.result
    #使用dfs ，每次加或者不加一个值
    def dfs(self, res, nums, index, size):
        if index == size:
            res_str = copy.deepcopy(res)
            print(res_str)
            self.result.append(res_str)
            return
        i = nums[index]
        res1 = res
        res2 = copy.deepcopy(res)
        res2.append(i)
        self.dfs(res1, nums, index + 1, size)
        self.dfs(res2, nums, index + 1, size)


if __name__ == "__main__":
    solution = Solution()
    solution.subsets([1, 2, 3])
