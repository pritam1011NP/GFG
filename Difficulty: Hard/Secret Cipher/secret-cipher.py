class Solution:
    def compress(self, s):
        n = len(s)

    # Build LPS array using KMP
        lps = [0] * n

        for i in range(1, n):
            j = lps[i - 1]

            while j > 0 and s[i] != s[j]:
                j = lps[j - 1]

            if s[i] == s[j]:
                j += 1

            lps[i] = j

    # Build answer from right to left
        ans = []
        i = n - 1

        while i >= 0:
        # A '*' can replace a repeated prefix
            if i % 2 == 1:
                length = i + 1
                prefix = lps[i]

                if (prefix >= length // 2 and
                    length % (2 * (length - prefix)) == 0):

                    ans.append('*')
                    i = i // 2
                    continue

            ans.append(s[i])
            i -= 1

        return ''.join(reversed(ans))