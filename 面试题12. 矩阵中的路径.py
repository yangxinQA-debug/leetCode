"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

 

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if board == None:
            return False
        h = len(board)
        w = len(board[0])
        for i in range(h):
            for j in range(w):
                grid = [[0 for j in range(w)] for i in range(h)]
                result = self.dfs(0, word, grid, board, i, j, h, w)
                if result:
                    return True
        return False

    def dfs(self, index, word, grid, board, i, j, h, w):
        grid[i][j] = 1
        if index == len(word) - 1:
            return True
        if word[index] != board[i][j]:
            return False
        if word[index] == board[i][j]:
            index += 1
        l, r, t, b = False, False, False, False
        if i - 1 > 0 and grid[i - 1][j] == 0:
            t = self.dfs(index, word, grid, board, i - 1, j, h, w)
        if i + 1 < h and grid[i + 1][j] == 0:
            b = self.dfs(index, word, grid, board, i + 1, j, h, w)
        if j - 1 > 0 and grid[i][j - 1] == 0:
            l = self.dfs(index, word, grid, board, i, j - 1, h, w)
        if j + 1 < w and grid[i][j + 1] == 0:
            r = self.dfs(index, word, grid, board, i, j + 1, h, w)
        return t or b or l or r


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    solution = Solution()
    print(solution.exist(board, word))
