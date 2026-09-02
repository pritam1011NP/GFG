class Solution:
    def maxDiffSum(self, arr):
        n = len(arr)

        if n <= 1:
            return 0

    # dp_original: maximum sum when current element is unchanged
    # dp_one: maximum sum when current element is replaced by 1

        dp_original = 0
        dp_one = 0

        for i in range(1, n):
        # Current element kept as original
            new_original = max(
                dp_original + abs(arr[i] - arr[i - 1]),
                dp_one + abs(arr[i] - 1)
            )

        # Current element replaced by 1
            new_one = max(
                dp_original + abs(1 - arr[i - 1]),
                dp_one + abs(1 - 1)
            )

            dp_original = new_original
            dp_one = new_one

        return max(dp_original, dp_one)