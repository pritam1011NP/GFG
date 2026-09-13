from collections import deque

class Solution:
    def partyHouse(self, adj: list[list[int]]) -> int:
        n = len(adj)

        if n <= 1:
            return 0

        def bfs(start):
            dist = [-1] * (n + 1)
            dist[start] = 0

            q = deque([start])
            farthest = start

            while q:
                u = q.popleft()

                for v in adj[u - 1]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)

                        if dist[v] > dist[farthest]:
                            farthest = v

            return farthest, dist[farthest]

        # Find one endpoint of the diameter
        node, _ = bfs(1)

        # Find the diameter length
        _, diameter = bfs(node)

        # Minimum maximum distance = radius
        return (diameter + 1) // 2