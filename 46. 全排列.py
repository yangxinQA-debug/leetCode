# -*-coding:utf-8
"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import copy


class Solution(object):
    def __init__(self):
        self.results = []
        self.res =[]

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        len_num = len(nums)
        self.permutation(nums, 0, len_num)

    def permutation(self, nums, index,  len_num):
        if index == len_num:
            print(self.res)
            self.results.append(self.res)
            return
        for i in range(len(nums)):
            self.res.append(nums[i])
            tmp = copy.deepcopy(nums)
            pop = nums.pop(i)
            self.permutation(nums, index + 1,  len_num)
            nums = tmp
            self.res = self.res[:-1]


if __name__ == "__main__":
    solution = Solution()
    result = solution.permute([1, 2,3])
    print(result)
