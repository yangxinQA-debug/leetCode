"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

示例 1:

输入:
11110
11010
11000
00000
输出: 1
示例 2:

输入:
11000
11000
00100
00011
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
题解：
https://leetcode-cn.com/problems/number-of-islands/solution/dao-yu-lei-wen-ti-de-tong-yong-jie-fa-dfs-bian-li-/
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        """
        思路，每发现一个小岛，沉没周围的陆地。
        """
        if len(grid) == 0:
            return 0
        h = len(grid)
        w = len(grid[0])
        count = 0
        for i in range(h):
            for j in range(w):
                if (grid[i][j]) == '1':
                    count += 1
                    # 沉默周围的陆地
                    self.sink(i, j, grid, h, w)
        print(count)
        return count

    def sink(self, m, n, grid, h, w):
        ## 深度优先遍历，沉没周围的陆地
        stack = [(m, n)]
        while (len(stack)):
            i, j = stack.pop()
            grid[i][j] = '0'
            if (i - 1 < 0 or grid[i - 1][j] == '0'):
                pass
            else:
                stack.append((i - 1, j))
            if (i + 1 > h - 1 or grid[i + 1][j] == '0'):
                pass
            else:
                stack.append((i + 1, j))
            if (j + 1 > w - 1 or grid[i][j + 1] == '0'):
                pass
            else:
                stack.append((i, j + 1))
            if (j - 1 < 0 or grid[i][j - 1] == '0'):
                pass
            else:
                stack.append((i, j - 1))


if __name__ == "__main__":
    grid = [[1, 1, 0, 0, 0, ],
            [1, 1, 0, 0, 0, ],
            [0, 0, 1, 0, 0, ],
            [0, 0, 0, 1, 1, ],
            ]
    grid2 = [
        [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]

    grid3 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    solution = Solution()
    solution.numIslands(grid3)
