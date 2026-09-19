class Solution:
    def findMinCost(self, s1: str, s2: str, costS1: int, costS2: int) -> int:
        n = len(s1)
        m = len(s2)

        # dp[j] = LCS length for s1 processed so far and s2[:j]
        dp = [0] * (m + 1)

        for i in range(1, n + 1):
            prev = 0

            for j in range(1, m + 1):
                temp = dp[j]

                if s1[i - 1] == s2[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])

                prev = temp

        lcs = dp[m]

        # Delete everything first, then subtract the cost saved
        # for every character kept in the common subsequence.
        total_cost = n * costS1 + m * costS2
        saved_cost = lcs * (costS1 + costS2)

        return total_cost - saved_cost