# -*-coding:utf-8
"""
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。
 
示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-window-maximum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
https://www.bilibili.com/video/av95531304?from=search&seid=12262877925598810207
"""

from collections import deque
class Solution(object):
    ### 1.递增队列
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        que = deque()
        que.append(nums[0])
        maxlist = []
        for i in range(0, len(nums)):
            ## 保证队列单调递增，如果后面加入的数大于队列里的数，就把队列里的数字退出。
            while (len(que) != 0 and nums[i] > que[0]):
                que.popleft()
            que.appendleft(nums[i])
            ## 保证最大值在窗口中，如果最大值已经滑出窗口，就把队列里的最大值弹出。
            while (i - k + 1 >= 0 and que[len(que) - 1] not in nums[i - k + 1:i + 1]):
                que.pop()
            if (i >= k - 1):
                # print(que[len(que) - 1])
                maxlist.append(que[len(que) - 1])
        print(maxlist)
        return maxlist


if __name__ == "__main__":
    solution = Solution()
    solution.maxSlidingWindow(nums=[1, 3, -1, -3, -2], k=3)
    # solution.maxSlidingWindow(nums=[1], k=1)
