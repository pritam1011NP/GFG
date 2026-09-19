class Solution:
    def largestSubsquare(self, mat):
        n = len(mat)

        # right[i][j] = consecutive X's starting at (i, j) going right
        # down[i][j]  = consecutive X's starting at (i, j) going down
        right = [[0] * n for _ in range(n)]
        down = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] == 'X':
                    right[i][j] = 1
                    down[i][j] = 1

                    if j + 1 < n:
                        right[i][j] += right[i][j + 1]

                    if i + 1 < n:
                        down[i][j] += down[i + 1][j]

        ans = 0

        for i in range(n):
            for j in range(n):
                # Maximum possible side from this top-left corner
                max_side = min(right[i][j], down[i][j])

                # Only need to check squares larger than current answer
                for side in range(max_side, ans, -1):
                    bottom = i + side - 1
                    right_col = j + side - 1

                    if bottom < n and right_col < n:
                        # Check bottom and right boundaries
                        if (right[bottom][j] >= side and
                                down[i][right_col] >= side):
                            ans = side
                            break

        return ans