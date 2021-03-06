# -*- coding:utf-8
"""
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

 

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
 

提示：

0 <= num < 231

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = len(str(num))
        if count == 0:
            return 0
        if count == 1:
            return 1
        dp = [0] * (count + 1)
        dp[0] = 1
        dp[1] = 1
        num_str = str(num)
        for i in range(2, count + 1):
            if num_str[i - 2] == '1' or (num_str[i - 2] == '2' and num_str[i - 1] < '6'):
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[count]


if __name__ == "__main__":
    solution = Solution()
    print(solution.translateNum(12258))
