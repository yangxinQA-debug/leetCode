# -*-coding:utf-8
"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        if (len(nums) < 3):
            print("can not found 3 nums")
            return []
        nums = sorted(nums)
        if (nums[0] > 0 or nums[len(nums) - 1] < 0):
            print("can not found 3 nums")
            return []
        i = 1
        while i < len(nums) - 1:
            lp = 0
            rp = len(nums) - 1
            j = i
            next_c = 0
            """
             寻找center
            """
            #对重复的数组，只计算一个C(中心)，来避免出现重复解
            while (i < len(nums) - 1 and nums[i] == nums[i + 1] ):
                i += 1
            #特殊情况要考虑到重复的两个大于0的数字需要都算入比如【-2，1，1】,这个时候要以左边的为center,才能算入右边的数字
            if (nums[i] > 0) and (nums[j] == nums[j + 1]):
                c = j
                ## 下一个center
                next_c = i + 1
             # 特殊情况要考虑到重复0的情况，当连续<3个0 的时候，不能构成和为0的3个数。当连续》=3个0 时，
            elif(nums[i] == 0) and (nums[j] == nums[j + 1]):
                c = i-1
            # 特殊情况要考虑到重复的两个小于0数字需要都算入比如【-1，-1，2】，这个时候，要以右边的为center,才能算入左边的数字
            else:
                c = i
            """
            对每一个center，查找和为0 的三个数
            """
            while (lp < c and c < rp):
                if (nums[lp] + nums[rp] + nums[c] == 0):
                    results.append((nums[lp], nums[rp], nums[c]))
                    while (nums[lp] == nums[lp + 1]) and (lp<c):
                        lp += 1
                    while (nums[rp] == nums[rp - 1]) and (rp>c):
                        rp -= 1
                    lp += 1
                    rp -= 1
                elif (nums[lp] + nums[rp] + nums[i] < 0) and (lp < c):
                    lp += 1
                elif (nums[lp] + nums[rp] + nums[i] > 0) and (rp > c):
                    rp -= 1

            i += 1
            #下一个center
            if next_c != 0:
                i = next_c
        print(results)
        return results


if __name__ == "__main__":
    solution = Solution()
    # nums = [-1, 0, 1, 2, -1, -4]
    # nums = [0, 0, 0, 0]
    nums = [3,0,-2,-1,1,2]
    nums = [-2, 0, 1, 1, 2]
    nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    nums = [-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0]
    nums = [1,1,-2]
    solution.threeSum(nums)
