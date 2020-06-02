# -*-coding:utf-8
"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import copy


class Solution(object):
    def __init__(self):
        self.results = []
        self.res = []

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size = len(nums)
        used = [False for _ in range(size)]
        nums = sorted(nums)
        self.permute(size, 0, used, nums)
        return self.results

    def permute(self, size, index, used, nums):
        if index == size:
            # copy.deepcopy 防止回溯时被改变
            copy_str = copy.deepcopy(self.res)
            self.results.append(copy_str)
            print(self.res)
            return
        for i in range(len(nums)):
            if used[i] == False:
                # used[i - 1] == False 两个数值相同的节点是并列关系，访问到第二个的时候，前一个已经退出。这种情况不需重复访问
                # used[i - 1] == True 两个数值相同的节点不是并列关系，访问到第二个节点时，第一个还没退出，第一个是第二个的父节点。这种情况，第二个几点还应加入path
                if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == False:
                    continue
                self.res.append(nums[i])
                used[i] = True
                self.permute(size, index + 1, used, nums)
                used[i] = False
                self.res.pop()


if __name__ == "__main__":
    solution = Solution()
    solution.permuteUnique([1, 1, 2])
