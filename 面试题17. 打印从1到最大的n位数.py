# -*- coding:utf-8
"""
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:

输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]
 

说明：

用返回一个整数列表来代替打印
n 为正整数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def __init__(self):
        self.results = []

    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        for i in range(0, 10):
            num = str(i)
            self.printNumsRecursively(1, num, n)
        return self.results

    def printNumsRecursively(self, index, num, n):
        if index == n:
            result = self.printNumber(num)
            if result:
                self.results.append(result)
            return
        for i in range(0, 10):
            num = str(i) + num
            self.printNumsRecursively(index + 1, num, n)
            num = num[1:]

    def printNumber(self, num):
        i = len(num) - 1
        result = 0
        while i >= 0 and num[i] == '0':
            i -= 1
        while i >= 0:
            result *= 10
            result += int(num[i])
            i -= 1
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.printNumbers(2))
