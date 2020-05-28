# -*- coding:utf-8
"""
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

 

示例 1:

输入: [1,2,3,4,5]
输出: True
 

示例 2:

输入: [0,0,1,2,5]
输出: True

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        res = sorted(nums)
        if 0 in res:
            count = 0
            for i in res:
                if i == 0:
                    count += 1
            gap = 0
            tmp = count
            for i in range(count + 1, len(nums)):
                if res[i] == res[tmp]:
                    return False
                if res[i] != res[tmp] + 1:
                    gap += res[i] - res[tmp] - 1
                tmp += 1
            if gap <= count:
                return True
            else:
                return False
        else:
            tmp = 0
            for i in range(1, len(nums)):
                if nums[i] != nums[tmp] + 1:
                    return False
                else:
                    tmp += 1
            return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isStraight([4, 1, 6, 0, 9]))
