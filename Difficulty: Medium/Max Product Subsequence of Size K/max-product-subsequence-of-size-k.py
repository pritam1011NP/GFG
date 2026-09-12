class Solution:
    def maxProduct(self, arr: list[int], k: int) -> int:
        INF = 10**30

        # max_dp[j] = maximum product using exactly j elements
        # min_dp[j] = minimum product using exactly j elements
        max_dp = [-INF] * (k + 1)
        min_dp = [INF] * (k + 1)

        max_dp[0] = 1
        min_dp[0] = 1

        for x in arr:
            # Traverse backwards so each element is used at most once
            for j in range(k, 0, -1):
                if max_dp[j - 1] == -INF:
                    continue

                candidates = [
                    max_dp[j - 1] * x,
                    min_dp[j - 1] * x
                ]

                max_dp[j] = max(max_dp[j], max(candidates))
                min_dp[j] = min(min_dp[j], min(candidates))

        return max_dp[k]