class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        for i in range(0, n):
            while (nums[i] != i):
                tmp = nums[i]
                # 如果nums[tmp] == tmp,表示nums[tmp]和nums[i]重复
                if (nums[tmp] == tmp):
                    return tmp
                else:
                    # 如果nums[tmp] != tmp,将nums[tmp]和nums[i] 互换
                    nums[i] = nums[tmp]
                    nums[tmp] = tmp
        return -1