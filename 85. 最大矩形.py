# -*-coding:utf-8
"""

给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6
"""


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        height_count = len(matrix)
        if height_count == 0:
            return 0
        width_count = len(matrix[0])
        max_area = 0
        for i in range(height_count):
            heights = [0] * width_count
            for j in range(i + 1):
                for k in range(width_count):
                    if matrix[j][k] == '0':
                        heights[k] = 0
                    else:
                        heights[k] += 1
            s = self.largestRectangleArea(heights)
            if s > max_area:
                max_area = s
        print(max_area)
        return max_area

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if (len(heights) == 0):
            return 0
        if (len(heights) == 1):
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
        # print(max_area)
        return max_area


if __name__ == "__main__":
    solution = Solution()
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    solution.maximalRectangle(matrix)
