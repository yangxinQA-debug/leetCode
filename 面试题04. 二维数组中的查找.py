class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix==[]:
            return False
        h = len(matrix)
        w = len(matrix[0])
        i = 0
        j = w - 1
        while i <= h-1 and j >= 0:
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                print("True")
                return True
        print("False")
        return False


if __name__ == "__main__":
    matrix = [[1, 4, 7, 11, 15],
              [2, 5, 8, 12, 19],
              [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    solution = Solution()
    solution.findNumberIn2DArray(matrix,
                                 20)