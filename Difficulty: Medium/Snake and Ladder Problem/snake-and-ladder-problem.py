from collections import deque

class Solution:
    def minThrows(self, n, lad, sn):
        N = n * n

        # jump[i] = destination if there is a snake/ladder at i
        jump = [-1] * (N + 1)

        # Ladders
        for i in range(0, len(lad), 2):
            start = lad[i]
            end = lad[i + 1]
            jump[start] = end

        # Snakes
        for i in range(0, len(sn), 2):
            start = sn[i]
            end = sn[i + 1]
            jump[start] = end

        # BFS: (current cell, number of throws)
        q = deque()
        q.append((1, 0))

        visited = [False] * (N + 1)
        visited[1] = True

        while q:
            cell, throws = q.popleft()

            if cell == N:
                return throws

            for dice in range(1, 7):
                nxt = cell + dice

                if nxt > N:
                    continue

                # Automatically take snake/ladder
                if jump[nxt] != -1:
                    nxt = jump[nxt]

                if not visited[nxt]:
                    visited[nxt] = True
                    q.append((nxt, throws + 1))

        return -1