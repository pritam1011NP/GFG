from collections import deque

class Solution:
    def numberOfCells(self, r: int, c: int, u: int, d: int, mat: list[list[int]]) -> int:
        n = len(mat)
        m = len(mat[0])

        # Starting cell is blocked
        if mat[r][c] == '#':
            return 0

        # dist[(x, y)] = minimum number of upward moves
        # required to reach (x, y)
        dist = {(r, c): 0}

        q = deque([(r, c)])

        directions = [
            (-1, 0, 1),  # up -> cost 1
            (1, 0, 0),   # down -> cost 0
            (0, -1, 0),  # left -> cost 0
            (0, 1, 0)    # right -> cost 0
        ]

        while q:
            x, y = q.popleft()
            curr = dist[(x, y)]

            for dx, dy, cost in directions:
                nx = x + dx
                ny = y + dy

                if not (0 <= nx < n and 0 <= ny < m):
                    continue

                if mat[nx][ny] == '#':
                    continue

                new_dist = curr + cost

                if (nx, ny) not in dist or new_dist < dist[(nx, ny)]:
                    dist[(nx, ny)] = new_dist

                    if cost == 0:
                        q.appendleft((nx, ny))
                    else:
                        q.append((nx, ny))

        # Count cells satisfying both constraints
        ans = 0

        for x, y in dist:
            up_moves = dist[(x, y)]

            # From:
            # down - up = x - r
            down_moves = up_moves + (x - r)

            if up_moves <= u and down_moves <= d:
                ans += 1

        return ans