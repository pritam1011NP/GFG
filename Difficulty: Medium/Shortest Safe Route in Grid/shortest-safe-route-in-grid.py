from collections import deque

class Solution:
    def shortestPath(self, mat: list[list[int]]) -> int:
        n = len(mat)
        m = len(mat[0])

        # Mark cells that are unsafe because they are mines
        # or adjacent to a mine.
        safe = [row[:] for row in mat]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    safe[i][j] = 0

                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < m:
                            safe[ni][nj] = 0

        # BFS from every safe cell in the first column.
        q = deque()

        for i in range(n):
            if safe[i][0] == 1:
                q.append((i, 0, 1))
                safe[i][0] = 0  # visited

        while q:
            i, j, dist = q.popleft()

            # Reached the last column
            if j == m - 1:
                return dist

            for di, dj in directions:
                ni, nj = i + di, j + dj

                if (
                    0 <= ni < n
                    and 0 <= nj < m
                    and safe[ni][nj] == 1
                ):
                    safe[ni][nj] = 0
                    q.append((ni, nj, dist + 1))

        return -1