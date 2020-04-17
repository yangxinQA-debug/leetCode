class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = 0
        p1 = len(s)
        for i in range(p1):
            if s[i] == ' ':
                count += 1
        p2 = p1 + count * 2
        for i in range(p2 - p1):
            s += ' '
        for j in range(p1 - 1, -1, -1):
            if s[j] != ' ' and j != p1 - 1:
                s = s[0:p2-1] + s[j] + s[p2:]
                p2 -= 1
            elif s[j] != ' ' and j == p1 - 1:
                s = s[0:p2 - 1] + s[j]
                p2 -= 1
            else:
                s = s[0:p2 - 1] + '0' + s[p2:]
                s = s[0:p2 - 2] + '2' + s[p2 - 1:]
                s = s[0:p2 - 3] + '%' + s[p2 - 2:]
                p2 -= 3
        print(s)
        return s


if __name__ == "__main__":
    solution = Solution()
    s = "We a"
    solution.replaceSpace(s)