"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
dp[i] 记录以i 为结尾的s[0:i]是否可拆分成字典里的单词。
j指向i,从后向前遍历：当找到一个位置j,使得s[j:i]为字典里单词，并且s[0:j-1]为可拆分的字符串，则s[0:i]可拆分。
若找不到j满足条件，ss[0:i] 不可拆分，i+=1，向后遍历更长的字符串
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True
        s = ' ' + s
        for i in range(1, len(s)):
            j = i
            while j > 0:
                if (s[j:i + 1] in wordDict and dp[j - 1] == True):
                    dp[i] = True
                j -= 1
        print(dp[len(s) - 1])
        return dp[len(s) - 1]

if __name__ == "__main__":
    solution = Solution()
    solution.wordBreak(s="leetcode", wordDict=["leet", "code"])
