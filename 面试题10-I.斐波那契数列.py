"""

"""


class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        for i in range(n):
            temp = a
            a = b
            b = temp + b
        return a


if __name__ == "__main__":
    solution = Solution()
    print(solution.fib(5))
