from bisect import bisect_right

class Solution:
    def dominantPairs(self, arr: list[int]) -> int:
        n = len(arr)
        half = n // 2

        first = arr[:half]
        second = sorted(arr[half:])

        count = 0

        for x in first:
            limit = x // 5
            count += bisect_right(second, limit)

        return count