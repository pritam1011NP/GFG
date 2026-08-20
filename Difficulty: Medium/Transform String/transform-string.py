class Solution:
    def transform(self, s1, s2):
        if len(s1) != len(s2):
            return -1

    # Same characters are necessary
        if sorted(s1) != sorted(s2):
            return -1

        i = len(s1) - 1
        j = len(s2) - 1

    # Find the longest suffix of s2 that already
    # appears in the same order in s1
        while i >= 0 and j >= 0:
            if s1[i] == s2[j]:
                i -= 1
                j -= 1
            else:
                i -= 1

    # Characters not part of the matched suffix
    # need to be moved to the front.
        return j + 1