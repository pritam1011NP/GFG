from bisect import bisect_left

class Solution:
    def getMarks(self, l, r, rank):
        # cumulative[i] = total number of valid marks
        # from interval 0 to i
        cumulative = []
        total = 0

        for i in range(len(l)):
            total += r[i] - l[i] + 1
            cumulative.append(total)

        ans = []

        for k in rank:
            # Find first interval whose cumulative count >= k
            idx = bisect_left(cumulative, k)

            # Number of valid marks before this interval
            before = cumulative[idx - 1] if idx > 0 else 0

            # Position inside the current interval (1-based)
            offset = k - before

            # Corresponding mark
            ans.append(l[idx] + offset - 1)

        return ans