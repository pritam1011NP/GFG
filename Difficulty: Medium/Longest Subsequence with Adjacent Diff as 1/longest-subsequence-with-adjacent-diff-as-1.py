class Solution:
    def longestSubseq(self, arr):
        dp = {}
        ans = 0

        for x in arr:
            # Best subsequence ending with x
            dp[x] = 1 + max(dp.get(x - 1, 0),
                            dp.get(x + 1, 0))

            ans = max(ans, dp[x])

        return ans