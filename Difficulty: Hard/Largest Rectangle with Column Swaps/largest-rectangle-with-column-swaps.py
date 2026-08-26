class Solution:
    def maxArea(self, mat: list[list[int]]) -> int:
        n = len(mat)
        m = len(mat[0])

        heights = [0] * m
        ans = 0

        for i in range(n):
        # Build histogram heights
            for j in range(m):
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

        # Since columns can be swapped,
        # sort heights in descending order.
            curr = sorted(heights, reverse=True)

        # Choose first j+1 columns, all having
        # height at least curr[j].
            for j in range(m):
                area = curr[j] * (j + 1)
                ans = max(ans, area)

        return ans