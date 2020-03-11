# -*-coding:utf-8
"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        j = 0
        w_length = 0
        max_length = 0
        char_set = {}
        """
        滑动窗口
        """
        while (i <= j and j < len(s)):
            if (s[j] in char_set):
                i = char_set[s[j]] + 1
                for key in char_set.keys():
                    if(char_set[key]<i):
                        char_set.pop(key)
                char_set[s[j]] = j
                j+=1
                w_length =j-i
            else:
                char_set[s[j]] = j
                j += 1
                w_length = j - i
                if w_length > max_length:
                    max_length = w_length
        print (max_length)
        return max_length


if __name__ == "__main__":
    solution = Solution()
    s = "tmmzuxt"
    solution.lengthOfLongestSubstring(s)
