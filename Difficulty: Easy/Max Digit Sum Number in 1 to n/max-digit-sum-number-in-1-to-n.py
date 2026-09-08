class Solution:
    def findMax(self, n):
        s = str(n)

        best = n
        best_sum = sum(int(d) for d in s)

        # Try decreasing each digit and making all following digits 9
        for i in range(len(s)):
            if s[i] == '0':
                continue

            candidate = int(s[:i] + str(int(s[i]) - 1) + '9' * (len(s) - i - 1))

            digit_sum = sum(int(d) for d in str(candidate))

            if digit_sum > best_sum or (digit_sum == best_sum and candidate > best):
                best = candidate
                best_sum = digit_sum

        return best