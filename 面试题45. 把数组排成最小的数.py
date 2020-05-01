"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

 

示例 1:

输入: [10,2]
输出: "102"
示例 2:

输入: [3,30,34,5,9]
输出: "3033459"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import functools
class Solution(object):
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        arrays = sorted(nums,key=functools.cmp_to_key(self.cmp_str))
        arrays = map(str, arrays)
        print("".join(arrays))
        return "".join(arrays)

    def cmp_str(self, int1, int2):
        s1 = str(int1)
        s2 = str(int2)
        # S1>S2 ,s1 应该排在S2的后面时返回1.
        if s1 + s2 < s2 + s1:
            return -1
        if s1 + s2 > s2 + s1:
            return 1
        if s1 + s2 == s2 + s1:
            return 0


if __name__ == "__main__":
    solution = Solution()
    solution.minNumber([3,30,34,5,9])
