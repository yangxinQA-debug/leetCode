# -*- coding:utf-8
"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。
输入: [2,1,5,6,2,3]
输出: 10
"""
"""
  使用单调队列，未遍历完heights 时 ，如果heights[i]>stack[top],在stack结尾加入heights[i]
  如果heights[i]<stack[top],计算top位置的面积：s=heights[stack[top]]*(i-1-stack[top-1]
"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if(len(heights)==0):
            return 0
        if(len(heights)==1):
            return heights[0]
        max_area = 0
        stack = [-1, 0]
        # 未遍历完heights 时
        for i in range(1, len(heights)):
            top = len(stack) - 1
            while (heights[i] < heights[stack[top]] and stack[top] >= 0):
                top = len(stack) - 1
                s = heights[stack[top]] * (i - 1 - stack[top - 1])
                stack.pop(-1)
                top -= 1
                if s > max_area:
                    max_area = s
            if (stack[top] >= 0 and heights[i] >= heights[stack[top]]) or (stack[top] < 0 and len(stack) == 1):
                stack.append(i)
                top += 1
                continue
        h = stack[top]
        # 遍历完heights 时
        while (len(stack) != 1):
            top = len(stack) - 1
            s = heights[stack[top]] * (h - stack[top - 1])
            stack.pop(-1)
            top -= 1
            if s > max_area:
                max_area = s
        print(max_area)
        return max_area


if __name__ == "__main__":
    solution = Solution()
    solution.largestRectangleArea([2, 1, 5, 6, 2, 3])
