class Solution:
    def formPyramid(self, arr):
        n = len(arr)

        left = [0] * n
        right = [0] * n

        # Maximum increasing height ending at i
        left[0] = 1
        for i in range(1, n):
            left[i] = min(arr[i], left[i - 1] + 1)

        # Maximum decreasing height starting at i
        right[n - 1] = 1
        for i in range(n - 2, -1, -1):
            right[i] = min(arr[i], right[i + 1] + 1)

        # Prefix sums of original array
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        total = prefix[n]
        min_cost = float('inf')

        for peak in range(n):
            h = min(left[peak], right[peak])

            # A pyramid of height h occupies [peak-h+1, peak+h-1]
            start = peak - h + 1
            end = peak + h - 1

            # Sum of pyramid heights:
            # 1 + 2 + ... + h + ... + 2 + 1
            pyramid_sum = h * h

            # Stones outside the pyramid must be reduced to 0
            # Inside, reduce them to the pyramid heights.
            current_sum = prefix[end + 1] - prefix[start]

            cost = total - pyramid_sum

            # The formula above already accounts for all reductions:
            # original total - final pyramid total.
            min_cost = min(min_cost, cost)

        return min_cost