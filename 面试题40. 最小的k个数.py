# -*- coding:utf-8
"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
"""
import random


class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k < 0:
            return None
        if k == len(arr):
            return arr
        return self.partitionArray(arr, 0, len(arr) - 1, k)

    def partitionArray(self, arr, l, h, k):
        index = self.partition(arr, l, h, k)
        while index != k:
            if index == k:
                return arr[:k]
            elif index < k:
                index = self.partition(arr, index + 1, h, k)
            elif index > k:
                index = self.partition(arr, l, index - 1, k)
        return arr[:k]

    def partition(self, arr, l, h, k):
        rand = random.randint(l, h)
        # rand =
        tmp = arr[l]
        arr[l] = arr[rand]
        arr[rand] = tmp
        tmp = arr[l]
        p, q = l, h
        while p < q:
            while arr[q] >= tmp and p < q:
                q -= 1
            arr[p] = arr[q]
            while arr[p] <= tmp and p < q:
                p += 1
            arr[q] = arr[p]
        arr[p] = tmp
        return p


if __name__ == "__main__":
    solution = Solution()
    print(solution.getLeastNumbers(arr=[3, 2, 1], k=2))
