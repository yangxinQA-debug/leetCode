# -*- coding:utf-8
"""
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
示例 1：

输入：nums = [3,4,3,3]
输出：4

示例 2：

输入：nums = [9,1,7,9,7,9,7]
输出：1
 
限制：
1 <= nums.length <= 1000
1 <= nums[i] < 2^31

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32):
            bit =1 << i
            cnt = 0
            for num in nums:
                if num & bit != 0:
                    cnt += 1
            if cnt % 3 != 0:
                 # 不等于0说明唯一出现的数字在这个 bit 上是1
                 res |= bit
        return res - 2 ** 32 if res > 2 ** 31 - 1 else res

