from bisect import bisect_right

class Solution:
    def findLongestWord(self, s: str, d: list) -> str:
        # Store positions of each character in s
        pos = [[] for _ in range(26)]

        for i, ch in enumerate(s):
            pos[ord(ch) - ord('a')].append(i)

        def is_subsequence(word):
            prev = -1

            for ch in word:
                positions = pos[ord(ch) - ord('a')]

                # Find first occurrence strictly after prev
                idx = bisect_right(positions, prev)

                if idx == len(positions):
                    return False

                prev = positions[idx]

            return True

        ans = ""

        for word in d:
            # No need to check shorter words
            if len(word) < len(ans):
                continue

            if is_subsequence(word):
                if (len(word) > len(ans) or
                    (len(word) == len(ans) and word < ans)):
                    ans = word

        return ans