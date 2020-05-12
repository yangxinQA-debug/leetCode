# -*- coding:utf-8
"""

给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m] 。请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
 

提示：

2 <= n <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
题解：
https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/solution/mian-shi-ti-14-ii-jian-sheng-zi-iitan-xin-er-fen-f/
"""

class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        p = 1e9 + 7
        if n < 3:
            return n - 1
        a = n // 3
        r = n % 3
        if r == 0:
            result = self.remainder(3, a, p)
        if r == 1:
            result = (self.remainder(3, a - 1, p) * 4) % p
        if r == 2:
            result = (self.remainder(3, a, p) * 2) % p
        return int(result)

    def remainder(self, x, a, p):
        """
        :param x: 底数
        :param a: 幂数
        :param p: 除数
        :return: (x^a)%p
        """
        ## (x^a)%p = (x^(a-1)%p * x)%p
        rem = 1
        for i in range(a):
            rem = (rem * x) % p
        return rem

if __name__ == "__main__":
    solution = Solution()
    print(solution.cuttingRope(10))