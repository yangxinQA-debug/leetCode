# -*- coding:utf-8
"""

根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
"""
"""
 用递减栈实现，当新遍历到的元素小于栈顶元素时，入栈
 当新遍历到的元素大于栈顶元素时，用新元素的下标减去栈顶下标，可求出距栈顶元素最近的高温天数
  题解：https://leetcode-cn.com/problems/daily-temperatures/solution/leetcode-tu-jie-739mei-ri-wen-du-by-misterbooo/
  
"""


class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        if len(T) == 0:
            return []
        stack = [(0, T[0])]
        result = [0 for i in range(len(T))]
        top = 0
        for i in range(1, len(T)):
            if T[i] <= stack[top][1]:
                stack.append((i, T[i]))
                top += 1
            else:
                while top >= 0 and T[i] > stack[top][1]:
                    distance = i - stack[top][0]
                    result[stack[top][0]] = distance
                    stack.pop()
                    top -= 1
                stack.append((i, T[i]))
                top += 1
        while top != -1:
            result[stack[top][0]] = 0
            top -= 1
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
