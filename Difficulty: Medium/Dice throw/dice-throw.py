class Solution:
    def noOfWays(self, m, n, x):
        # dp[j] = number of ways to get sum j
        dp = [0] * (x + 1)
        dp[0] = 1
        
        for _ in range(n):  # for each dice
            new_dp = [0] * (x + 1)
            
            for j in range(x + 1):
                if dp[j] != 0:
                    for face in range(1, m + 1):
                        if j + face <= x:
                            new_dp[j + face] += dp[j]
            
            dp = new_dp
        
        return dp[x]