class Solution:
    def countSubsequences(self, s, n):
        MOD = 10**9 + 7

    # dp[r] = number of non-empty subsequences
    # whose value has remainder r when divided by n
        dp = [0] * n

        for ch in s:
            digit = int(ch)

        # Take a copy because we need the old dp values
        # while processing the current digit.
            new_dp = dp[:]

        # Start a new subsequence with this digit
            new_dp[digit % n] = (new_dp[digit % n] + 1) % MOD

        # Append current digit to every existing subsequence
            for r in range(n):
                if dp[r]:
                    new_rem = (r * 10 + digit) % n
                    new_dp[new_rem] = (new_dp[new_rem] + dp[r]) % MOD

            dp = new_dp

        return dp[0]