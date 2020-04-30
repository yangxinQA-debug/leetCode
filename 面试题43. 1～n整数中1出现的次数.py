# -*-coding:utf-8
"""
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。

例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

示例 1：

输入：n = 12
输出：5
示例 2：

输入：n = 13
输出：6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        return self.NumberOf1(n)

    def NumberOf1(self, n):
        first = int(str(n)[0])
        length = len(str(n))
        numfirstDigit = 0
        if first > 1:
            numfirstDigit = self.power10base(length - 1)
        if first == 1 and n>=10:
            numfirstDigit = int(str(n)[1:]) + 1
        elif n==1:
            numfirstDigit = 1
        numOtherDigits = first * (length - 1) * self.power10base(length - 2)
        if n >= 10:
            nextNumber = int(str(n)[1:])
            numRecursive = self.NumberOf1(nextNumber)
        else:
            numRecursive = 0
        return numfirstDigit + numOtherDigits + numRecursive

    def power10base(self, n):
        result = 1
        for i in range(n):
            result *= 10
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.countDigitOne(10))
