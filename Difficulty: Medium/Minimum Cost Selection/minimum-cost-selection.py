class Solution:
    def minCost(self, mat):
        # dp[j] = minimum cost when choice j is selected
        # for the previous row
        dp = mat[0][:]

        for i in range(1, len(mat)):
            curr = [0] * 3

            curr[0] = mat[i][0] + min(dp[1], dp[2])
            curr[1] = mat[i][1] + min(dp[0], dp[2])
            curr[2] = mat[i][2] + min(dp[0], dp[1])

            dp = curr

        return min(dp)