class Solution:
    def minCost(self, n: int, i: int, d: int, c: int) -> int:
        # dp(x) = minimum cost to create exactly x characters
        # Starting from 1 character.
        from functools import lru_cache

        @lru_cache(None)
        def dp(x):
            if x == 1:
                return i

            # Option 1: create x using only insertions
            ans = x * i

            # If x is even:
            # Build x//2 and copy-paste once.
            if x % 2 == 0:
                ans = min(ans, dp(x // 2) + c)

            else:
                # Option 2:
                # Build x//2, copy -> x-1, then insert 1
                half = x // 2
                ans = min(
                    ans,
                    dp(half) + c + i
                )

                # Option 3:
                # Build (x+1)//2, copy -> x+1, then delete 1
                half = (x + 1) // 2
                ans = min(
                    ans,
                    dp(half) + c + d
                )

            return ans

        return dp(n)