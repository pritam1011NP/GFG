class Solution:
    def searchWord(self, mat, word):
        n = len(mat)
        m = len(mat[0])
        k = len(word)

        # 8 possible directions
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        ans = []

        for i in range(n):
            for j in range(m):

                # First character must match
                if mat[i][j] != word[0]:
                    continue

                # Check all 8 directions
                found = False

                for dr, dc in directions:
                    x, y = i, j
                    idx = 0

                    while idx < k:
                        if x < 0 or x >= n or y < 0 or y >= m:
                            break

                        if mat[x][y] != word[idx]:
                            break

                        x += dr
                        y += dc
                        idx += 1

                    if idx == k:
                        found = True
                        break

                if found:
                    ans.append([i, j])

        return ans