class Solution:
    def minMoves(self, arr):
        n = len(arr)

    # position[value] = index of value in arr
        position = [0] * (n + 1)

        for i, value in enumerate(arr):
            position[value] = i

    # Find the longest consecutive sequence of values
    # that already appear in the correct order.
        longest = 1
        current = 1

        for value in range(1, n):
            if position[value] < position[value + 1]:
                current += 1
            else:
                current = 1

            longest = max(longest, current)

        return n - longest