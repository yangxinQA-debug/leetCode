# -*- coding:utf-8
"""
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

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
链接：https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import deque


class Solution(object):
    """
    j指向每次滑入的值
    window[i,j]表示滑动窗口，i 的范围[ -k+1, len(nums)-k] ,j 的范围[0,len(nums)-1],i,j 每次前进一格
    deque 用一个递减队列deque[0] 为当前滑动窗口的最大值 。
    deque[0] 和滑出的i 值相同，弹出window[0]
    滑入windows[j]时，将deque 中比window[j]小的数字popleft 弹出。保证deque为递减的队列，deque[0]为当前窗口内的最大值
    每次窗口滑动一步，res 增加window[0]
    """

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        i, j = -k, -1
        que = deque()
        res = []
        while i < len(nums) - k:
            # 滑出处理
            if len(que) >= 1 and i >= 0 and nums[i] == que[0]:
                que.popleft()
            i += 1
            # 滑入处理：
            j += 1
            l = len(que)-1
            # que 内所有小于nums[j]的数弹出
            while len(que) >= 1 and l>=0:
                if que[l] < nums[j]:
                    que.pop()
                l -= 1
            que.append(nums[j])
            # 记录当前窗口最大值
            if j >= k - 1:
                res.append(que[0])
        return res


if __name__ == "__main__":
    nums = [1, 3, 1, 2, 0, 5]
    k = 3
    solution = Solution()
    print(solution.maxSlidingWindow(nums, k))
