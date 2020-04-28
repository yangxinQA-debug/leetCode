# -*-coding:utf-8
"""

实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。


示例 1:

输入: 2.00000, 10
输出: 1024.00000
"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == 1:
            return x
        if n<0:
            return 1/self.myPow(x,-n)
        result = self.myPow(x, n << 1) * self.myPow(x, n << 1)
        if n & 0x1 == 1:
            result = result * x
        return result
